import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.color_name import ColorName
from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.doc_text import DocText


T = TypeVar("T", bound="Doc")


@_attrs_define
class Doc:
    """
    Attributes:
        duid (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        in_trash (bool):
        folder_duid (str):
        order (str):
        title (str):
        text (DocText):
        edited_by_ai (bool):
        editor_duids (List[str]):
        subscriber_duids (List[str]):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_name (ColorName): * `Red` - RED
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
        updated_by_client_duid (Union[Unset, None, str]):
        drafter_duid (Optional[str]):
        recommendation_duid (Optional[str]):
    """

    duid: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    in_trash: bool
    folder_duid: str
    order: str
    title: str
    text: "DocText"
    edited_by_ai: bool
    editor_duids: List[str]
    subscriber_duids: List[str]
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_name: ColorName
    drafter_duid: Optional[str]
    recommendation_duid: Optional[str]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        in_trash = self.in_trash
        folder_duid = self.folder_duid
        order = self.order
        title = self.title
        text = self.text.to_dict()

        edited_by_ai = self.edited_by_ai
        editor_duids = self.editor_duids

        subscriber_duids = self.subscriber_duids

        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji
        color_name = self.color_name.value

        updated_by_client_duid = self.updated_by_client_duid
        drafter_duid = self.drafter_duid
        recommendation_duid = self.recommendation_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "inTrash": in_trash,
                "folderDuid": folder_duid,
                "order": order,
                "title": title,
                "text": text,
                "editedByAi": edited_by_ai,
                "editorDuids": editor_duids,
                "subscriberDuids": subscriber_duids,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorName": color_name,
                "drafterDuid": drafter_duid,
                "recommendationDuid": recommendation_duid,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.doc_text import DocText

        d = src_dict.copy()
        duid = d.pop("duid")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        in_trash = d.pop("inTrash")

        folder_duid = d.pop("folderDuid")

        order = d.pop("order")

        title = d.pop("title")

        text = DocText.from_dict(d.pop("text"))

        edited_by_ai = d.pop("editedByAi")

        editor_duids = cast(List[str], d.pop("editorDuids"))

        subscriber_duids = cast(List[str], d.pop("subscriberDuids"))

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_name = ColorName(d.pop("colorName"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        drafter_duid = d.pop("drafterDuid")

        recommendation_duid = d.pop("recommendationDuid")

        doc = cls(
            duid=duid,
            created_at=created_at,
            updated_at=updated_at,
            in_trash=in_trash,
            folder_duid=folder_duid,
            order=order,
            title=title,
            text=text,
            edited_by_ai=edited_by_ai,
            editor_duids=editor_duids,
            subscriber_duids=subscriber_duids,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_name=color_name,
            updated_by_client_duid=updated_by_client_duid,
            drafter_duid=drafter_duid,
            recommendation_duid=recommendation_duid,
        )

        doc.additional_properties = d
        return doc

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
