from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.subtask_display_mode import SubtaskDisplayMode

T = TypeVar("T", bound="LayoutConfig")


@_attrs_define
class LayoutConfig:
    """
    Attributes:
        subtask_display_mode (SubtaskDisplayMode): * `1` - INDENTED
            * `2` - COLLAPSED
            * `3` - FLAT
        show_absentees (bool):
    """

    subtask_display_mode: SubtaskDisplayMode
    show_absentees: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subtask_display_mode = self.subtask_display_mode.value

        show_absentees = self.show_absentees

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subtaskDisplayMode": subtask_display_mode,
                "showAbsentees": show_absentees,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        subtask_display_mode = SubtaskDisplayMode(d.pop("subtaskDisplayMode"))

        show_absentees = d.pop("showAbsentees")

        layout_config = cls(
            subtask_display_mode=subtask_display_mode,
            show_absentees=show_absentees,
        )

        layout_config.additional_properties = d
        return layout_config

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
