from enum import Enum


class EventKind(str, Enum):
    AICONTENT = "ai/content"
    AIEMOJI = "ai/emoji"
    AIFEEDBACK = "ai/feedback"
    AIICON = "ai/icon"
    AIPROPS = "ai/props"
    AISUBTASKS = "ai/subtasks"
    AITRANSLATE = "ai/translate"
    DOCSCREATE = "docs/create"
    DOCSDELETE = "docs/delete"
    DOCSUPDATE_OTHER = "docs/update_other"
    DOCSUPDATE_TITLE = "docs/update_title"
    HELPRESOURCE_CLICK = "help/resource_click"
    ONBOARDINGFINISH_STEP = "onboarding/finish_step"
    PAGESCREATE = "pages/create"
    PAGESDELETE = "pages/delete"
    PAGESROLLOVER = "pages/rollover"
    PAGESUPDATE_OTHER = "pages/update_other"
    PAGESUPDATE_PERMISSIONS = "pages/update_permissions"
    PAGESUPDATE_TITLE = "pages/update_title"
    PROFILEBECOME_ACTIVE = "profile/become_active"
    PROFILEBECOME_INACTIVE = "profile/become_inactive"
    PROFILEDELETE = "profile/delete"
    PROFILEUPDATE = "profile/update"
    TASKSCOMMENT = "tasks/comment"
    TASKSCREATE = "tasks/create"
    TASKSDELETE = "tasks/delete"
    TASKSDELETE_FULLY = "tasks/delete_fully"
    TASKSDUE_DATE_TOMORROW = "tasks/due_date_tomorrow"
    TASKSREMINDER_NOW = "tasks/reminder_now"
    TASKSREMOVE_RELATIONSHIP = "tasks/remove_relationship"
    TASKSSET_RELATIONSHIP = "tasks/set_relationship"
    TASKSUPDATE_ASSIGNEES = "tasks/update_assignees"
    TASKSUPDATE_DESCRIPTION = "tasks/update_description"
    TASKSUPDATE_OTHER = "tasks/update_other"
    TASKSUPDATE_STATUS = "tasks/update_status"
    TASKSUPDATE_SUBSCRIPTIONS = "tasks/update_subscriptions"
    TASKSUPDATE_TITLE = "tasks/update_title"
    USAGECOPY_BRANCH = "usage/copy_branch"
    USAGECOPY_TASK_LINK = "usage/copy_task_link"
    USAGENLP_RAW_CREATE = "usage/nlp_raw_create"
    USAGENLP_RAW_DELETE = "usage/nlp_raw_delete"
    USAGENLP_TYPEAHEAD_ACCEPT = "usage/nlp_typeahead_accept"
    USAGENLP_TYPEAHEAD_OPEN = "usage/nlp_typeahead_open"
    USAGEOPEN_COMMAND_CENTER = "usage/open_command_center"
    USAGEOPEN_FULLSCREEN = "usage/open_fullscreen"
    USAGEOPEN_RIGHTBAR = "usage/open_rightbar"
    USAGEOPEN_SEARCH = "usage/open_search"
    USAGEREDO = "usage/redo"
    USAGESUBMIT_FEEDBACK = "usage/submit_feedback"
    USAGEUNDO = "usage/undo"
    WORKSPACEBECOME_ACTIVE = "workspace/become_active"
    WORKSPACEBECOME_INACTIVE = "workspace/become_inactive"
    WORKSPACECREATE = "workspace/create"
    WORKSPACEDATA_EXPORT = "workspace/data_export"
    WORKSPACEDATA_IMPORT = "workspace/data_import"
    WORKSPACEDELETE = "workspace/delete"
    WORKSPACEDOWNGRADE_FINALIZE = "workspace/downgrade_finalize"
    WORKSPACEDOWNGRADE_INITIALIZE = "workspace/downgrade_initialize"
    WORKSPACEINVITE = "workspace/invite"
    WORKSPACEJOIN = "workspace/join"
    WORKSPACELEAVE = "workspace/leave"
    WORKSPACEUPDATE_OTHER = "workspace/update_other"
    WORKSPACEUPDATE_PROPERTY = "workspace/update_property"
    WORKSPACEUPDATE_STATUS = "workspace/update_status"
    WORKSPACEUPGRADE = "workspace/upgrade"

    def __str__(self) -> str:
        return str(self.value)
