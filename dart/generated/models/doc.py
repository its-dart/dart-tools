import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.icon_kind import IconKind
from ..models.report_kind import ReportKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Doc")


@_attrs_define
class Doc:
    """
    Attributes:
        duid (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        drafter_duid (Union[None, str]):
        in_trash (bool):
        folder_duid (str):
        report_kind (Union[None, ReportKind]):
        order (str):
        title (str):
        text (Any):
        edited_by_ai (bool):
        recommendation_duid (Union[None, str]):
        editor_duids (list[str]):
        subscriber_duids (list[str]):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
        updated_by_client_duid (Union[None, Unset, str]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    drafter_duid: Union[None, str]
    in_trash: bool
    folder_duid: str
    report_kind: Union[None, ReportKind]
    order: str
    title: str
    text: Any
    edited_by_ai: bool
    recommendation_duid: Union[None, str]
    editor_duids: list[str]
    subscriber_duids: list[str]
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    updated_by_client_duid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        drafter_duid: Union[None, str]
        drafter_duid = self.drafter_duid

        in_trash = self.in_trash

        folder_duid = self.folder_duid

        report_kind: Union[None, str]
        if isinstance(self.report_kind, ReportKind):
            report_kind = self.report_kind.value
        else:
            report_kind = self.report_kind

        order = self.order

        title = self.title

        text = self.text

        edited_by_ai = self.edited_by_ai

        recommendation_duid: Union[None, str]
        recommendation_duid = self.recommendation_duid

        editor_duids = self.editor_duids

        subscriber_duids = self.subscriber_duids

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        updated_by_client_duid: Union[None, Unset, str]
        if isinstance(self.updated_by_client_duid, Unset):
            updated_by_client_duid = UNSET
        else:
            updated_by_client_duid = self.updated_by_client_duid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "drafterDuid": drafter_duid,
                "inTrash": in_trash,
                "folderDuid": folder_duid,
                "reportKind": report_kind,
                "order": order,
                "title": title,
                "text": text,
                "editedByAi": edited_by_ai,
                "recommendationDuid": recommendation_duid,
                "editorDuids": editor_duids,
                "subscriberDuids": subscriber_duids,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_drafter_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid"))

        in_trash = d.pop("inTrash")

        folder_duid = d.pop("folderDuid")

        def _parse_report_kind(data: object) -> Union[None, ReportKind]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_kind_type_0 = ReportKind(data)

                return report_kind_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ReportKind], data)

        report_kind = _parse_report_kind(d.pop("reportKind"))

        order = d.pop("order")

        title = d.pop("title")

        text = d.pop("text")

        edited_by_ai = d.pop("editedByAi")

        def _parse_recommendation_duid(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid"))

        editor_duids = cast(list[str], d.pop("editorDuids"))

        subscriber_duids = cast(list[str], d.pop("subscriberDuids"))

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        def _parse_updated_by_client_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        updated_by_client_duid = _parse_updated_by_client_duid(d.pop("updatedByClientDuid", UNSET))

        doc = cls(
            duid=duid,
            created_at=created_at,
            updated_at=updated_at,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            folder_duid=folder_duid,
            report_kind=report_kind,
            order=order,
            title=title,
            text=text,
            edited_by_ai=edited_by_ai,
            recommendation_duid=recommendation_duid,
            editor_duids=editor_duids,
            subscriber_duids=subscriber_duids,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            updated_by_client_duid=updated_by_client_duid,
        )

        doc.additional_properties = d
        return doc

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
