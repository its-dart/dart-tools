from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.color_name import ColorName
from ..models.folder_kind import FolderKind
from ..models.icon_kind import IconKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Folder")


@_attrs_define
class Folder:
    """
    Attributes:
        duid (str):
        space_duid (str):
        kind (FolderKind): * `Other` - OTHER
            * `Default` - DEFAULT
            * `Reports` - REPORTS
        order (str):
        title (str):
        description (str):
        icon_kind (IconKind): * `None` - NONE
            * `Icon` - ICON
            * `Emoji` - EMOJI
        icon_name_or_emoji (str):
        color_hex (str):
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
    """

    duid: str
    space_duid: str
    kind: FolderKind
    order: str
    title: str
    description: str
    icon_kind: IconKind
    icon_name_or_emoji: str
    color_hex: str
    color_name: ColorName
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        space_duid = self.space_duid
        kind = self.kind.value

        order = self.order
        title = self.title
        description = self.description
        icon_kind = self.icon_kind.value

        icon_name_or_emoji = self.icon_name_or_emoji
        color_hex = self.color_hex
        color_name = self.color_name.value

        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "spaceDuid": space_duid,
                "kind": kind,
                "order": order,
                "title": title,
                "description": description,
                "iconKind": icon_kind,
                "iconNameOrEmoji": icon_name_or_emoji,
                "colorHex": color_hex,
                "colorName": color_name,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        space_duid = d.pop("spaceDuid")

        kind = FolderKind(d.pop("kind"))

        order = d.pop("order")

        title = d.pop("title")

        description = d.pop("description")

        icon_kind = IconKind(d.pop("iconKind"))

        icon_name_or_emoji = d.pop("iconNameOrEmoji")

        color_hex = d.pop("colorHex")

        color_name = ColorName(d.pop("colorName"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        folder = cls(
            duid=duid,
            space_duid=space_duid,
            kind=kind,
            order=order,
            title=title,
            description=description,
            icon_kind=icon_kind,
            icon_name_or_emoji=icon_name_or_emoji,
            color_hex=color_hex,
            color_name=color_name,
            updated_by_client_duid=updated_by_client_duid,
        )

        folder.additional_properties = d
        return folder

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
