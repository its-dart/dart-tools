from enum import Enum


class TaskLinkKind(str, Enum):
    GITHUB_BRANCH = "GitHub Branch"
    GITHUB_EXPANSION = "GitHub Expansion"
    GITHUB_PULL_REQUEST = "GitHub Pull Request"
    NOTION_DOCUMENT = "Notion Document"
    NOTION_DOCUMENT_DOESNT_EXIST = "Notion Document Doesnt Exist"
    NOTION_DOCUMENT_PARSE_FAILED = "Notion Document Parse Failed"
    NOTION_EXPANSION = "Notion Expansion"
    NOTION_LINK = "Notion Link"
    SLACK_EXPANSION = "Slack Expansion"
    SOURCE_FROM_TEMPLATE = "Source From Template"
    SOURCE_FROM_THIRD_PARTY = "Source From Third Party"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
