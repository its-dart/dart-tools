from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
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
        source_user (Union[Unset, None, str]):
        source_type (Union[Unset, DocSourceType]): * `Unknown` - UNKNOWN
            * `Onboarding` - ONBOARDING
            * `Recommendation` - RECOMMENDATION
            * `GeneratedReport` - GENERATED_REPORT
            * `ChatGPT` - CHAT_GPT
            * `Application` - APPLICATION Default: DocSourceType.UNKNOWN.
        drafter_duid (Union[Unset, None, str]):
        in_trash (Union[Unset, bool]):
        folder_duid (Union[Unset, str]):
        report_kind (Union[Unset, None, ReportKind]): * `Standup` - STANDUP
            * `Changelog` - CHANGELOG
        order (Union[Unset, str]):
        title (Union[Unset, str]):
        text (Union[Unset, Any]):
        text_markdown (Union[Unset, str]):
        edited_by_ai (Union[Unset, bool]):
        recommendation_duid (Union[Unset, None, str]):
        editor_duids (Union[Unset, List[str]]):
        subscriber_duids (Union[Unset, List[str]]):
        icon_kind (Union[Unset, IconKind]): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (Union[Unset, str]):
        color_hex (Union[Unset, str]):
        color_name (Union[Unset, ColorName]): * `Red` - RED
            * `Dark Blue` - DARK_BLUE
            * `Dark Orange` - DARK_ORANGE
            * `Dark Green` - DARK_GREEN
            * `Purple` - PURPLE
            * `Dark Teal` - DARK_TEAL
            * `Pink` - PINK
            * `Orange` - ORANGE
            * `Green` - GREEN
            * `Yellow` - YELLOW
            * `Brown` - BROWN
            * `Dark Red` - DARK_RED
            * `Flat Green` - FLAT_GREEN
            * `Red Orange` - RED_ORANGE
            * `Teal` - TEAL
            * `Light Green` - LIGHT_GREEN
            * `Light Blue` - LIGHT_BLUE
            * `Light Purple` - LIGHT_PURPLE
            * `Light Orange` - LIGHT_ORANGE
            * `Light Pink` - LIGHT_PINK
            * `Tan` - TAN
            * `Dark Gray` - DARK_GRAY
            * `Light Brown` - LIGHT_BROWN
            * `Light Gray` - LIGHT_GRAY
    """

    duid: str
    source_user: Union[Unset, None, str] = UNSET
    source_type: Union[Unset, DocSourceType] = DocSourceType.UNKNOWN
    drafter_duid: Union[Unset, None, str] = UNSET
    in_trash: Union[Unset, bool] = UNSET
    folder_duid: Union[Unset, str] = UNSET
    report_kind: Union[Unset, None, ReportKind] = UNSET
    order: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    text: Union[Unset, Any] = UNSET
    text_markdown: Union[Unset, str] = UNSET
    edited_by_ai: Union[Unset, bool] = UNSET
    recommendation_duid: Union[Unset, None, str] = UNSET
    editor_duids: Union[Unset, List[str]] = UNSET
    subscriber_duids: Union[Unset, List[str]] = UNSET
    icon_kind: Union[Unset, IconKind] = UNSET
    icon_name_or_emoji: Union[Unset, str] = UNSET
    color_hex: Union[Unset, str] = UNSET
    color_name: Union[Unset, ColorName] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        source_user = self.source_user
        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        drafter_duid = self.drafter_duid
        in_trash = self.in_trash
        folder_duid = self.folder_duid
        report_kind: Union[Unset, None, str] = UNSET
        if not isinstance(self.report_kind, Unset):
            report_kind = self.report_kind.value if self.report_kind else None

        order = self.order
        title = self.title
        text = self.text
        text_markdown = self.text_markdown
        edited_by_ai = self.edited_by_ai
        recommendation_duid = self.recommendation_duid
        editor_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.editor_duids, Unset):
            editor_duids = self.editor_duids

        subscriber_duids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subscriber_duids, Unset):
            subscriber_duids = self.subscriber_duids

        icon_kind: Union[Unset, str] = UNSET
        if not isinstance(self.icon_kind, Unset):
            icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji
        color_hex = self.color_hex
        color_name: Union[Unset, str] = UNSET
        if not isinstance(self.color_name, Unset):
            color_name = self.color_name.value

        field_dict: Dict[str, Any] = {}
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
        if color_name is not UNSET:
            field_dict["colorName"] = color_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        source_user = d.pop("sourceUser", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, DocSourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = DocSourceType(_source_type)

        drafter_duid = d.pop("drafterDuid", UNSET)

        in_trash = d.pop("inTrash", UNSET)

        folder_duid = d.pop("folderDuid", UNSET)

        _report_kind = d.pop("reportKind", UNSET)
        report_kind: Union[Unset, None, ReportKind]
        if _report_kind is None:
            report_kind = None
        elif isinstance(_report_kind, Unset):
            report_kind = UNSET
        else:
            report_kind = ReportKind(_report_kind)

        order = d.pop("order", UNSET)

        title = d.pop("title", UNSET)

        text = d.pop("text", UNSET)

        text_markdown = d.pop("textMarkdown", UNSET)

        edited_by_ai = d.pop("editedByAi", UNSET)

        recommendation_duid = d.pop("recommendationDuid", UNSET)

        editor_duids = cast(List[str], d.pop("editorDuids", UNSET))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids", UNSET))

        _icon_kind = d.pop("iconKind", UNSET)
        icon_kind: Union[Unset, IconKind]
        if isinstance(_icon_kind, Unset):
            icon_kind = UNSET
        else:
            icon_kind = IconKind(_icon_kind)

        icon_name_or_emoji = d.pop("iconNameOrEmoji", UNSET)

        color_hex = d.pop("colorHex", UNSET)

        _color_name = d.pop("colorName", UNSET)
        color_name: Union[Unset, ColorName]
        if isinstance(_color_name, Unset):
            color_name = UNSET
        else:
            color_name = ColorName(_color_name)

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
            color_name=color_name,
        )

        doc_create.additional_properties = d
        return doc_create

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
