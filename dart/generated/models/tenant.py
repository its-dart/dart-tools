import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.subscription import Subscription

if TYPE_CHECKING:
    from ..models.discord_integration import DiscordIntegration
    from ..models.github_integration import GithubIntegration
    from ..models.notion_integration import NotionIntegration
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
        backlog_enabled (bool):
        ai_assignment_enabled (bool):
        email_integration_enabled (bool):
        copy_parent_fields_on_create (bool):
        webhook_enabled (bool):
        webhook_secret (str):
        image_url (Optional[str]):
        webhook_url (Optional[str]):
        notion_integration (Optional[NotionIntegration]):
        slack_integration (Optional[SlackIntegration]):
        discord_integration (Optional[DiscordIntegration]):
        github_integration (Optional[GithubIntegration]):
        zapier_integration (Optional[ZapierIntegration]):
    """

    duid: str
    is_dart: bool
    name: str
    created_at: datetime.datetime
    timezone: str
    subscription: Subscription
    entitlement_overrides: Any
    backlog_enabled: bool
    ai_assignment_enabled: bool
    email_integration_enabled: bool
    copy_parent_fields_on_create: bool
    webhook_enabled: bool
    webhook_secret: str
    image_url: Optional[str]
    webhook_url: Optional[str]
    notion_integration: Optional["NotionIntegration"]
    slack_integration: Optional["SlackIntegration"]
    discord_integration: Optional["DiscordIntegration"]
    github_integration: Optional["GithubIntegration"]
    zapier_integration: Optional["ZapierIntegration"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        is_dart = self.is_dart
        name = self.name
        created_at = self.created_at.isoformat()

        timezone = self.timezone
        subscription = self.subscription.value

        entitlement_overrides = self.entitlement_overrides
        backlog_enabled = self.backlog_enabled
        ai_assignment_enabled = self.ai_assignment_enabled
        email_integration_enabled = self.email_integration_enabled
        copy_parent_fields_on_create = self.copy_parent_fields_on_create
        webhook_enabled = self.webhook_enabled
        webhook_secret = self.webhook_secret
        image_url = self.image_url
        webhook_url = self.webhook_url
        notion_integration = self.notion_integration.to_dict() if self.notion_integration else None

        slack_integration = self.slack_integration.to_dict() if self.slack_integration else None

        discord_integration = self.discord_integration.to_dict() if self.discord_integration else None

        github_integration = self.github_integration.to_dict() if self.github_integration else None

        zapier_integration = self.zapier_integration.to_dict() if self.zapier_integration else None

        field_dict: Dict[str, Any] = {}
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
                "backlogEnabled": backlog_enabled,
                "aiAssignmentEnabled": ai_assignment_enabled,
                "emailIntegrationEnabled": email_integration_enabled,
                "copyParentFieldsOnCreate": copy_parent_fields_on_create,
                "webhookEnabled": webhook_enabled,
                "webhookSecret": webhook_secret,
                "imageUrl": image_url,
                "webhookUrl": webhook_url,
                "notionIntegration": notion_integration,
                "slackIntegration": slack_integration,
                "discordIntegration": discord_integration,
                "githubIntegration": github_integration,
                "zapierIntegration": zapier_integration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.discord_integration import DiscordIntegration
        from ..models.github_integration import GithubIntegration
        from ..models.notion_integration import NotionIntegration
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

        backlog_enabled = d.pop("backlogEnabled")

        ai_assignment_enabled = d.pop("aiAssignmentEnabled")

        email_integration_enabled = d.pop("emailIntegrationEnabled")

        copy_parent_fields_on_create = d.pop("copyParentFieldsOnCreate")

        webhook_enabled = d.pop("webhookEnabled")

        webhook_secret = d.pop("webhookSecret")

        image_url = d.pop("imageUrl")

        webhook_url = d.pop("webhookUrl")

        _notion_integration = d.pop("notionIntegration")
        notion_integration: Optional[NotionIntegration]
        if _notion_integration is None:
            notion_integration = None
        else:
            notion_integration = NotionIntegration.from_dict(_notion_integration)

        _slack_integration = d.pop("slackIntegration")
        slack_integration: Optional[SlackIntegration]
        if _slack_integration is None:
            slack_integration = None
        else:
            slack_integration = SlackIntegration.from_dict(_slack_integration)

        _discord_integration = d.pop("discordIntegration")
        discord_integration: Optional[DiscordIntegration]
        if _discord_integration is None:
            discord_integration = None
        else:
            discord_integration = DiscordIntegration.from_dict(_discord_integration)

        _github_integration = d.pop("githubIntegration")
        github_integration: Optional[GithubIntegration]
        if _github_integration is None:
            github_integration = None
        else:
            github_integration = GithubIntegration.from_dict(_github_integration)

        _zapier_integration = d.pop("zapierIntegration")
        zapier_integration: Optional[ZapierIntegration]
        if _zapier_integration is None:
            zapier_integration = None
        else:
            zapier_integration = ZapierIntegration.from_dict(_zapier_integration)

        tenant = cls(
            duid=duid,
            is_dart=is_dart,
            name=name,
            created_at=created_at,
            timezone=timezone,
            subscription=subscription,
            entitlement_overrides=entitlement_overrides,
            backlog_enabled=backlog_enabled,
            ai_assignment_enabled=ai_assignment_enabled,
            email_integration_enabled=email_integration_enabled,
            copy_parent_fields_on_create=copy_parent_fields_on_create,
            webhook_enabled=webhook_enabled,
            webhook_secret=webhook_secret,
            image_url=image_url,
            webhook_url=webhook_url,
            notion_integration=notion_integration,
            slack_integration=slack_integration,
            discord_integration=discord_integration,
            github_integration=github_integration,
            zapier_integration=zapier_integration,
        )

        tenant.additional_properties = d
        return tenant

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
