from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.doc_source_type import DocSourceType
from ..models.icon_kind import IconKind
from ..models.report_kind import ReportKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocCreate")


@_attrs_define
class DocCreate:
    """
    Attributes:
        duid (str):
        source_user (Union[None, Unset, str]):
        source_type (Union[Unset, DocSourceType]): * `Unknown` - UNKNOWN
            * `Onboarding` - ONBOARDING
            * `Recommendation` - RECOMMENDATION
            * `GeneratedReport` - GENERATED_REPORT
            * `ChatGPT` - CHAT_GPT
            * `Application` - APPLICATION Default: DocSourceType.UNKNOWN.
        drafter_duid (Union[None, Unset, str]):
        in_trash (Union[Unset, bool]):
        folder_duid (Union[Unset, str]):
        report_kind (Union[None, ReportKind, Unset]):
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        text (Union[Unset, Any]):
        text_markdown (Union[Unset, str]):
        edited_by_ai (Union[Unset, bool]):
        recommendation_duid (Union[None, Unset, str]):
        editor_duids (Union[Unset, list[str]]):
        subscriber_duids (Union[Unset, list[str]]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
    """

    duid: str
    source_user: Union[None, Unset, str] = UNSET
    source_type: Union[Unset, DocSourceType] = DocSourceType.UNKNOWN
    drafter_duid: Union[None, Unset, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    folder_duid: Union[Unset, str] = UNSET
    report_kind: Union[None, ReportKind, Unset] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    text: Union[Unset, Any] = UNSET
    text_markdown: Union[Unset, str] = UNSET
    edited_by_ai: Union[Unset, bool] = UNSET
    recommendation_duid: Union[None, Unset, str] = UNSET
    editor_duids: Union[Unset, list[str]] = UNSET
    subscriber_duids: Union[Unset, list[str]] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        source_user: Union[None, Unset, str]
        if isinstance(self.source_user, Unset):
            source_user = UNSET
        else:
            source_user = self.source_user

        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        drafter_duid: Union[None, Unset, str]
        if isinstance(self.drafter_duid, Unset):
            drafter_duid = UNSET
        else:
            drafter_duid = self.drafter_duid

        in_trash = self.in_trash

        folder_duid = self.folder_duid

        report_kind: Union[None, Unset, str]
        if isinstance(self.report_kind, Unset):
            report_kind = UNSET
        elif isinstance(self.report_kind, ReportKind):
            report_kind = self.report_kind.value
        else:
            report_kind = self.report_kind

        order = self.order

        title = self.title

        text = self.text

        text_markdown = self.text_markdown

        edited_by_ai = self.edited_by_ai

        recommendation_duid: Union[None, Unset, str]
        if isinstance(self.recommendation_duid, Unset):
            recommendation_duid = UNSET
        else:
            recommendation_duid = self.recommendation_duid

        editor_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.editor_duids, Unset):
            editor_duids = self.editor_duids

        subscriber_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.subscriber_duids, Unset):
            subscriber_duids = self.subscriber_duids

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji

        color_hex = self.color_hex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if source_user is not UNSET:
            field_dict["sourceUser"] = source_user
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if drafter_duid is not UNSET:
            field_dict["drafterDuid"] = drafter_duid
        if in_trash is not UNSET:
            field_dict["inTrash"] = in_trash
        if folder_duid is not UNSET:
            field_dict["folderDuid"] = folder_duid
        if report_kind is not UNSET:
            field_dict["reportKind"] = report_kind
        if order is not UNSET:
            field_dict["order"] = order
        if title is not UNSET:
            field_dict["title"] = title
        if text is not UNSET:
            field_dict["text"] = text
        if text_markdown is not UNSET:
            field_dict["textMarkdown"] = text_markdown
        if edited_by_ai is not UNSET:
            field_dict["editedByAi"] = edited_by_ai
        if recommendation_duid is not UNSET:
            field_dict["recommendationDuid"] = recommendation_duid
        if editor_duids is not UNSET:
            field_dict["editorDuids"] = editor_duids
        if subscriber_duids is not UNSET:
            field_dict["subscriberDuids"] = subscriber_duids
        if icon_kind is not UNSET:
            field_dict["iconKind"] = icon_kind
        if icon_name_or_emoji is not UNSET:
            field_dict["iconNameOrEmoji"] = icon_name_or_emoji
        if color_hex is not UNSET:
            field_dict["colorHex"] = color_hex

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        def _parse_source_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        source_user = _parse_source_user(d.pop("sourceUser", UNSET))

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, DocSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = DocSourceType(_source_type)

        def _parse_drafter_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        drafter_duid = _parse_drafter_duid(d.pop("drafterDuid", UNSET))

        in_trash = d.pop("inTrash", UNSET)

        folder_duid = d.pop("folderDuid", UNSET)

        def _parse_report_kind(data: object) -> Union[None, ReportKind, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                report_kind_type_0 = ReportKind(data)

                return report_kind_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, ReportKind, Unset], data)

        report_kind = _parse_report_kind(d.pop("reportKind", UNSET))

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        text = d.pop("text", UNSET)

        text_markdown = d.pop("textMarkdown", UNSET)

        edited_by_ai = d.pop("editedByAi", UNSET)

        def _parse_recommendation_duid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        recommendation_duid = _parse_recommendation_duid(d.pop("recommendationDuid", UNSET))

        editor_duids = cast(list[str], d.pop("editorDuids", UNSET))

        subscriber_duids = cast(list[str], d.pop("subscriberDuids", UNSET))

        _icon_kind = d.pop("iconKind", UNSET)
        icon_kind: Union[Unset, IconKind]
        if isinstance(_icon_kind, Unset):
            icon_kind = UNSET
        else:
            icon_kind = IconKind(_icon_kind)

        icon_name_or_emoji = d.pop("iconNameOrEmoji", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        doc_create = cls(
            duid=duid,
            source_user=source_user,
            source_type=source_type,
            drafter_duid=drafter_duid,
            in_trash=in_trash,
            folder_duid=folder_duid,
            report_kind=report_kind,
            order=order,
            title=title,
            text=text,
            text_markdown=text_markdown,
            edited_by_ai=edited_by_ai,
            recommendation_duid=recommendation_duid,
            editor_duids=editor_duids,
            subscriber_duids=subscriber_duids,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
        )

        doc_create.additional_properties = d
        return doc_create

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
