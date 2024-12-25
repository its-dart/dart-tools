import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription import Subscription

if TYPE_CHECKING:
    from ..models.discord_integration import DiscordIntegration
    from ..models.github_integration import GithubIntegration
    from ..models.notion_integration import NotionIntegration
    from ..models.saml_config import SamlConfig
    from ..models.slack_integration import SlackIntegration
    from ..models.zapier_integration import ZapierIntegration


T = TypeVar("T", bound="Tenant")


@_attrs_define
class Tenant:
    """
    Attributes:
        duid (str):
        is_dart (bool):
        name (str):
        created_at (datetime.datetime):
        timezone (str):
        subscription (Subscription): * `Personal` - PERSONAL
            * `Premium` - PREMIUM
        entitlement_overrides (Any):
        image_url (Union[None, str]):
        backlog_enabled (bool):
        ai_assignment_enabled (bool):
        email_integration_enabled (bool):
        close_parent_on_close_all_subtasks (bool):
        move_subtasks_on_move_parent (bool):
        update_subtasks_status_on_update_parent_status (bool):
        copy_parent_fields_on_create (bool):
        update_blockee_dates_on_update_blocker_due_date (bool):
        webhook_enabled (bool):
        webhook_secret (str):
        saml_config (Union['SamlConfig', None]):
        notion_integration (Union['NotionIntegration', None]):
        slack_integration (Union['SlackIntegration', None]):
        discord_integration (Union['DiscordIntegration', None]):
        github_integration (Union['GithubIntegration', None]):
        zapier_integration (Union['ZapierIntegration', None]):
    """

    duid: str
    is_dart: bool
    name: str
    created_at: datetime.datetime
    timezone: str
    subscription: Subscription
    entitlement_overrides: Any
    image_url: Union[None, str]
    backlog_enabled: bool
    ai_assignment_enabled: bool
    email_integration_enabled: bool
    close_parent_on_close_all_subtasks: bool
    move_subtasks_on_move_parent: bool
    update_subtasks_status_on_update_parent_status: bool
    copy_parent_fields_on_create: bool
    update_blockee_dates_on_update_blocker_due_date: bool
    webhook_enabled: bool
    webhook_secret: str
    saml_config: Union["SamlConfig", None]
    notion_integration: Union["NotionIntegration", None]
    slack_integration: Union["SlackIntegration", None]
    discord_integration: Union["DiscordIntegration", None]
    github_integration: Union["GithubIntegration", None]
    zapier_integration: Union["ZapierIntegration", None]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.discord_integration import DiscordIntegration
        from ..models.github_integration import GithubIntegration
        from ..models.notion_integration import NotionIntegration
        from ..models.saml_config import SamlConfig
        from ..models.slack_integration import SlackIntegration
        from ..models.zapier_integration import ZapierIntegration

        duid = self.duid

        is_dart = self.is_dart

        name = self.name

        created_at = self.created_at.isoformat()

        timezone = self.timezone

        subscription = self.subscription.value

        entitlement_overrides = self.entitlement_overrides

        image_url: Union[None, str]
        image_url = self.image_url

        backlog_enabled = self.backlog_enabled

        ai_assignment_enabled = self.ai_assignment_enabled

        email_integration_enabled = self.email_integration_enabled

        close_parent_on_close_all_subtasks = self.close_parent_on_close_all_subtasks

        move_subtasks_on_move_parent = self.move_subtasks_on_move_parent

        update_subtasks_status_on_update_parent_status = self.update_subtasks_status_on_update_parent_status

        copy_parent_fields_on_create = self.copy_parent_fields_on_create

        update_blockee_dates_on_update_blocker_due_date = self.update_blockee_dates_on_update_blocker_due_date

        webhook_enabled = self.webhook_enabled

        webhook_secret = self.webhook_secret

        saml_config: Union[None, dict[str, Any]]
        if isinstance(self.saml_config, SamlConfig):
            saml_config = self.saml_config.to_dict()
        else:
            saml_config = self.saml_config

        notion_integration: Union[None, dict[str, Any]]
        if isinstance(self.notion_integration, NotionIntegration):
            notion_integration = self.notion_integration.to_dict()
        else:
            notion_integration = self.notion_integration

        slack_integration: Union[None, dict[str, Any]]
        if isinstance(self.slack_integration, SlackIntegration):
            slack_integration = self.slack_integration.to_dict()
        else:
            slack_integration = self.slack_integration

        discord_integration: Union[None, dict[str, Any]]
        if isinstance(self.discord_integration, DiscordIntegration):
            discord_integration = self.discord_integration.to_dict()
        else:
            discord_integration = self.discord_integration

        github_integration: Union[None, dict[str, Any]]
        if isinstance(self.github_integration, GithubIntegration):
            github_integration = self.github_integration.to_dict()
        else:
            github_integration = self.github_integration

        zapier_integration: Union[None, dict[str, Any]]
        if isinstance(self.zapier_integration, ZapierIntegration):
            zapier_integration = self.zapier_integration.to_dict()
        else:
            zapier_integration = self.zapier_integration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "isDart": is_dart,
                "name": name,
                "createdAt": created_at,
                "timezone": timezone,
                "subscription": subscription,
                "entitlementOverrides": entitlement_overrides,
                "imageUrl": image_url,
                "backlogEnabled": backlog_enabled,
                "aiAssignmentEnabled": ai_assignment_enabled,
                "emailIntegrationEnabled": email_integration_enabled,
                "closeParentOnCloseAllSubtasks": close_parent_on_close_all_subtasks,
                "moveSubtasksOnMoveParent": move_subtasks_on_move_parent,
                "updateSubtasksStatusOnUpdateParentStatus": update_subtasks_status_on_update_parent_status,
                "copyParentFieldsOnCreate": copy_parent_fields_on_create,
                "updateBlockeeDatesOnUpdateBlockerDueDate": update_blockee_dates_on_update_blocker_due_date,
                "webhookEnabled": webhook_enabled,
                "webhookSecret": webhook_secret,
                "samlConfig": saml_config,
                "notionIntegration": notion_integration,
                "slackIntegration": slack_integration,
                "discordIntegration": discord_integration,
                "githubIntegration": github_integration,
                "zapierIntegration": zapier_integration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.discord_integration import DiscordIntegration
        from ..models.github_integration import GithubIntegration
        from ..models.notion_integration import NotionIntegration
        from ..models.saml_config import SamlConfig
        from ..models.slack_integration import SlackIntegration
        from ..models.zapier_integration import ZapierIntegration

        d = src_dict.copy()
        duid = d.pop("duid")

        is_dart = d.pop("isDart")

        name = d.pop("name")

        created_at = isoparse(d.pop("createdAt"))

        timezone = d.pop("timezone")

        subscription = Subscription(d.pop("subscription"))

        entitlement_overrides = d.pop("entitlementOverrides")

        def _parse_image_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        image_url = _parse_image_url(d.pop("imageUrl"))

        backlog_enabled = d.pop("backlogEnabled")

        ai_assignment_enabled = d.pop("aiAssignmentEnabled")

        email_integration_enabled = d.pop("emailIntegrationEnabled")

        close_parent_on_close_all_subtasks = d.pop("closeParentOnCloseAllSubtasks")

        move_subtasks_on_move_parent = d.pop("moveSubtasksOnMoveParent")

        update_subtasks_status_on_update_parent_status = d.pop("updateSubtasksStatusOnUpdateParentStatus")

        copy_parent_fields_on_create = d.pop("copyParentFieldsOnCreate")

        update_blockee_dates_on_update_blocker_due_date = d.pop("updateBlockeeDatesOnUpdateBlockerDueDate")

        webhook_enabled = d.pop("webhookEnabled")

        webhook_secret = d.pop("webhookSecret")

        def _parse_saml_config(data: object) -> Union["SamlConfig", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                saml_config_type_0 = SamlConfig.from_dict(data)

                return saml_config_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SamlConfig", None], data)

        saml_config = _parse_saml_config(d.pop("samlConfig"))

        def _parse_notion_integration(data: object) -> Union["NotionIntegration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                notion_integration_type_0 = NotionIntegration.from_dict(data)

                return notion_integration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NotionIntegration", None], data)

        notion_integration = _parse_notion_integration(d.pop("notionIntegration"))

        def _parse_slack_integration(data: object) -> Union["SlackIntegration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                slack_integration_type_0 = SlackIntegration.from_dict(data)

                return slack_integration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SlackIntegration", None], data)

        slack_integration = _parse_slack_integration(d.pop("slackIntegration"))

        def _parse_discord_integration(data: object) -> Union["DiscordIntegration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                discord_integration_type_0 = DiscordIntegration.from_dict(data)

                return discord_integration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DiscordIntegration", None], data)

        discord_integration = _parse_discord_integration(d.pop("discordIntegration"))

        def _parse_github_integration(data: object) -> Union["GithubIntegration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                github_integration_type_0 = GithubIntegration.from_dict(data)

                return github_integration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["GithubIntegration", None], data)

        github_integration = _parse_github_integration(d.pop("githubIntegration"))

        def _parse_zapier_integration(data: object) -> Union["ZapierIntegration", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                zapier_integration_type_0 = ZapierIntegration.from_dict(data)

                return zapier_integration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ZapierIntegration", None], data)

        zapier_integration = _parse_zapier_integration(d.pop("zapierIntegration"))

        tenant = cls(
            duid=duid,
            is_dart=is_dart,
            name=name,
            created_at=created_at,
            timezone=timezone,
            subscription=subscription,
            entitlement_overrides=entitlement_overrides,
            image_url=image_url,
            backlog_enabled=backlog_enabled,
            ai_assignment_enabled=ai_assignment_enabled,
            email_integration_enabled=email_integration_enabled,
            close_parent_on_close_all_subtasks=close_parent_on_close_all_subtasks,
            move_subtasks_on_move_parent=move_subtasks_on_move_parent,
            update_subtasks_status_on_update_parent_status=update_subtasks_status_on_update_parent_status,
            copy_parent_fields_on_create=copy_parent_fields_on_create,
            update_blockee_dates_on_update_blocker_due_date=update_blockee_dates_on_update_blocker_due_date,
            webhook_enabled=webhook_enabled,
            webhook_secret=webhook_secret,
            saml_config=saml_config,
            notion_integration=notion_integration,
            slack_integration=slack_integration,
            discord_integration=discord_integration,
            github_integration=github_integration,
            zapier_integration=zapier_integration,
        )

        tenant.additional_properties = d
        return tenant

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
