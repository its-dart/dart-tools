from enum import Enum


class TaskKind(str, Enum):
    BUG = "Bug"
    CLIENT = "Client"
    EPIC = "Epic"
    ISSUE = "Issue"
    ITEM = "Item"
    MILESTONE = "Milestone"
    PROJECT = "Project"
    SPIKE = "Spike"
    STORY = "Story"
    SUBISSUE = "Subissue"
    SUBTASK = "Subtask"
    TASK = "Task"

    def __str__(self) -> str:
        return str(self.value)
