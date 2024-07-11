from enum import Enum


class EventKind(str, Enum):
    AIBRAINSTORM_START = "ai/brainstorm_start"
    AICONTENT = "ai/content"
    AIDETECT_DUPLICATES = "ai/detect_duplicates"
    AIEMOJI = "ai/emoji"
    AIEXECUTE = "ai/execute"
    AIFEEDBACK = "ai/feedback"
    AIFILTERS = "ai/filters"
    AIICON = "ai/icon"
    AIIMAGE = "ai/image"
    AIPLAN = "ai/plan"
    AIPROPS = "ai/props"
    AIREPORT = "ai/report"
    AISUBTASKS = "ai/subtasks"
    AITRANSLATE = "ai/translate"
    BRAINSTORMSTART = "brainstorm/start"
    BRAINSTORMSTOP = "brainstorm/stop"
    DOCSCREATE = "docs/create"
    DOCSDELETE = "docs/delete"
    DOCSUPDATE_OTHER = "docs/update_other"
    DOCSUPDATE_TITLE = "docs/update_title"
    HELPRESOURCE_CLICK = "help/resource_click"
    LOADAPP = "load/app"
    LOADAUTHENTICATE = "load/authenticate"
    LOADSIGNUP = "load/signup"
    LOADUNIDLE = "load/unidle"
    ONBOARDINGFINISH_STEP = "onboarding/finish_step"
    PAGESCREATE = "pages/create"
    PAGESDELETE = "pages/delete"
    PAGESROLLOVER = "pages/rollover"
    PAGESUPDATE_OTHER = "pages/update_other"
    PAGESUPDATE_PERMISSIONS = "pages/update_permissions"
    PAGESUPDATE_TITLE = "pages/update_title"
    PROFILEBECOME_ACTIVE = "profile/become_active"
    PROFILEBECOME_INACTIVE = "profile/become_inactive"
    PROFILECREATE = "profile/create"
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
    USAGEOPEN_TASK_OVERLAY = "usage/open_task_overlay"
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
