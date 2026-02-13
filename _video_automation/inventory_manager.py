"""

Inventory Management System

Tracks production inventory across all stages: prompts -> images -> slides -> audio -> video

"""



import json

from pathlib import Path

from typing import Dict, List, Optional

from datetime import datetime

from dataclasses import dataclass, asdict

from enum import Enum





class InventoryStage(Enum):

    """Production stages"""

    PROMPTS = "prompts"

    IMAGES = "images"

    SLIDES = "slides"

    AUDIO = "audio"

    VIDEO = "video"





@dataclass

class ProjectInventory:

    """Inventory status for a single project"""

    name: str

    pptx_path: str

    project_dir: str



    # Counts

    total_slides: int = 0

    prompts_generated: int = 0

    images_ready: int = 0

    images_manual: int = 0

    images_generated: int = 0

    slides_created: bool = False

    audio_ready: int = 0

    video_created: bool = False



    # Timestamps

    created_at: str = ""

    updated_at: str = ""



    # Status

    current_stage: str = "prompts"

    completion_percent: int = 0



    def update_stage(self):

        """Determine current stage based on progress"""

        if self.video_created:

            self.current_stage = "video_complete"

            self.completion_percent = 100

        elif self.audio_ready >= self.total_slides and self.total_slides > 0:

            self.current_stage = "audio_complete"

            self.completion_percent = 90

        elif self.slides_created:

            self.current_stage = "slides_complete"

            self.completion_percent = 70

        elif self.images_ready >= self.total_slides and self.total_slides > 0:

            self.current_stage = "images_complete"

            self.completion_percent = 50

        elif self.prompts_generated >= self.total_slides and self.total_slides > 0:

            self.current_stage = "prompts_complete"

            self.completion_percent = 20

        else:

            self.current_stage = "in_progress"

            if self.total_slides > 0:

                self.completion_percent = int((self.prompts_generated / self.total_slides) * 20)



    def is_ready_for_next_stage(self) -> Optional[str]:

        """Check if ready for next stage"""

        if self.current_stage == "prompts_complete" and self.images_ready < self.total_slides:

            return "Generate images"

        elif self.current_stage == "images_complete" and not self.slides_created:

            return "Create slides"

        elif self.current_stage == "slides_complete" and self.audio_ready < self.total_slides:

            return "Generate audio"

        elif self.current_stage == "audio_complete" and not self.video_created:

            return "Create video"

        return None





class InventoryManager:

    """Manages production inventory across all projects"""



    def __init__(self, base_dir: str = "_projects"):

        self.base_dir = Path(base_dir)

        self.base_dir.mkdir(exist_ok=True)

        self.inventory_file = self.base_dir / "inventory.json"

        self.projects: Dict[str, ProjectInventory] = {}

        self.load()



    def load(self):

        """Load inventory from disk"""

        if self.inventory_file.exists():

            try:

                with open(self.inventory_file, 'r') as f:

                    data = json.load(f)

                    for name, proj_data in data.items():

                        self.projects[name] = ProjectInventory(**proj_data)

            except Exception as e:

                print(f"Warning: Could not load inventory: {e}")



    def save(self):

        """Save inventory to disk"""

        try:

            data = {name: asdict(proj) for name, proj in self.projects.items()}

            with open(self.inventory_file, 'w') as f:

                json.dump(data, f, indent=2)

        except Exception as e:

            print(f"Warning: Could not save inventory: {e}")



    def scan_project(self, project_name: str, project_dir: Path) -> ProjectInventory:

        """Scan project directory and update inventory"""



        # Get or create project inventory

        if project_name in self.projects:

            project = self.projects[project_name]

        else:

            project = ProjectInventory(

                name=project_name,

                pptx_path="",

                project_dir=str(project_dir),

                created_at=datetime.now().isoformat()

            )



        project.updated_at = datetime.now().isoformat()



        # Count prompts

        prompt_dir = project_dir / "image_prompts"

        if prompt_dir.exists():

            prompts = list(prompt_dir.glob("slide_*.txt"))

            project.prompts_generated = len(prompts)

            project.total_slides = max(project.total_slides, len(prompts))



        # Count images

        image_dir = project_dir / "images"

        if image_dir.exists():

            images = list(image_dir.glob("slide_*.png"))

            images += list(image_dir.glob("slide_*.jpg"))

            project.images_ready = len(images)



        # Check for slides

        slides_dir = project_dir / "slides_rendered"

        redesigned_pptx = list(project_dir.glob("*_redesigned.pptx"))

        project.slides_created = slides_dir.exists() or len(redesigned_pptx) > 0



        # Count audio files

        output_dir = project_dir / "output"

        if output_dir.exists():

            audio_files = list(output_dir.glob("slide_*_audio*.wav"))

            project.audio_ready = len(audio_files)



            # Check for video

            video_files = list(output_dir.glob("*.mp4"))

            project.video_created = len(video_files) > 0



        # Update stage

        project.update_stage()



        self.projects[project_name] = project

        self.save()



        return project



    def scan_all_projects(self):

        """Scan all projects in base directory"""

        for proj_dir in self.base_dir.iterdir():

            if proj_dir.is_dir() and proj_dir.name != "__pycache__":

                self.scan_project(proj_dir.name, proj_dir)



    def get_dashboard(self) -> str:

        """Generate inventory dashboard"""

        lines = []

        lines.append("==")

        lines.append("|           PRODUCTION INVENTORY DASHBOARD                     |")

        lines.append("==")

        lines.append("")



        if not self.projects:

            lines.append("No projects in inventory yet.")

            lines.append("")

            lines.append("To add projects:")

            lines.append("  python slide_redesigner.py presentation.pptx --plan-only")

            return "\n".join(lines)



        # Summary stats

        total_projects = len(self.projects)

        completed = sum(1 for p in self.projects.values() if p.video_created)

        in_progress = total_projects - completed



        lines.append(f"Total Projects: {total_projects}")

        lines.append(f"  Completed: {completed}")

        lines.append(f"  In Progress: {in_progress}")

        lines.append("")



        # Group by stage

        by_stage = {}

        for proj in self.projects.values():

            stage = proj.current_stage

            if stage not in by_stage:

                by_stage[stage] = []

            by_stage[stage].append(proj)



        # Show each stage

        stage_order = [

            ("in_progress", "[WAIT] STARTING"),

            ("prompts_complete", "[PROMPTS] PROMPTS READY"),

            ("images_complete", "[IMAGES] IMAGES READY"),

            ("slides_complete", "[SLIDES] SLIDES READY"),

            ("audio_complete", "[AUDIO][\!]  AUDIO READY"),

            ("video_complete", "[OK] VIDEOS COMPLETE"),

        ]



        for stage_key, stage_label in stage_order:

            projects_in_stage = by_stage.get(stage_key, [])

            if projects_in_stage:

                lines.append(stage_label)

                lines.append("+" + "-" * 58 + "+")



                for proj in projects_in_stage:

                    # Progress bar

                    bar_length = 20

                    filled = int((proj.completion_percent / 100) * bar_length)

                    bar = "#" * filled + "." * (bar_length - filled)



                    lines.append(f"| {proj.name[:30]:<30}")

                    lines.append(f"|   [{bar}] {proj.completion_percent}%")



                    # Details

                    if proj.total_slides > 0:

                        details = []

                        if proj.prompts_generated > 0:

                            details.append(f"Prompts: {proj.prompts_generated}/{proj.total_slides}")

                        if proj.images_ready > 0:

                            details.append(f"Images: {proj.images_ready}/{proj.total_slides}")

                        if proj.slides_created:

                            details.append("Slides: [OK]")

                        if proj.audio_ready > 0:

                            details.append(f"Audio: {proj.audio_ready}/{proj.total_slides}")

                        if proj.video_created:

                            details.append("Video: [OK]")



                        if details:

                            lines.append(f"|   {' | '.join(details)}")



                    # Next action

                    next_action = proj.is_ready_for_next_stage()

                    if next_action:

                        lines.append(f"|   -> Next: {next_action}")



                    lines.append("|")



                lines.append("+" + "-" * 58 + "+")

                lines.append("")



        # API quota status (if available)

        lines.append("=" * 60)

        lines.append("NEXT ACTIONS:")

        lines.append("")



        # Suggest actions

        actions = []

        for proj in self.projects.values():

            next_action = proj.is_ready_for_next_stage()

            if next_action:

                actions.append(f"  * {proj.name}: {next_action}")



        if actions:

            lines.extend(actions)

        else:

            lines.append("  [OK] All projects at current stage completion")



        return "\n".join(lines)



    def get_pending_work(self, stage: InventoryStage) -> List[ProjectInventory]:

        """Get projects that need work at specific stage"""

        pending = []



        for proj in self.projects.values():

            if stage == InventoryStage.PROMPTS:

                if proj.total_slides > 0 and proj.prompts_generated < proj.total_slides:

                    pending.append(proj)

            elif stage == InventoryStage.IMAGES:

                if proj.prompts_generated > 0 and proj.images_ready < proj.prompts_generated:

                    pending.append(proj)

            elif stage == InventoryStage.SLIDES:

                if proj.images_ready > 0 and not proj.slides_created:

                    pending.append(proj)

            elif stage == InventoryStage.AUDIO:

                if proj.slides_created and proj.audio_ready < proj.total_slides:

                    pending.append(proj)

            elif stage == InventoryStage.VIDEO:

                if proj.audio_ready >= proj.total_slides and not proj.video_created:

                    pending.append(proj)



        return pending





def main():

    """Test inventory manager"""

    inventory = InventoryManager()



    print("Scanning all projects...")

    inventory.scan_all_projects()



    print("\n" + inventory.get_dashboard())



    # Show pending work

    pending_images = inventory.get_pending_work(InventoryStage.IMAGES)

    if pending_images:

        print(f"\n{len(pending_images)} projects need images generated")





if __name__ == "__main__":

    main()

