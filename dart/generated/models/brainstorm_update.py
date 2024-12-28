import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.brainstorm_state import BrainstormState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrainstormUpdate")


@_attrs_define
class BrainstormUpdate:
    """
    Attributes:
        duid (str):
        dartboard_duid (Union[Unset, str]):
        subject (Union[Unset, str]):
        ai (Union[Unset, bool]):
        total_session_ms (Union[Unset, int]):
        started_at (Union[Unset, datetime.datetime]):
        state (Union[Unset, BrainstormState]): * `Running` - RUNNING
            * `Paused` - PAUSED
            * `Stopped` - STOPPED
        after_start_ms (Union[Unset, int]):
        created_tasks_duids (Union[Unset, list[str]]):
    """

    duid: str
    dartboard_duid: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    ai: Union[Unset, bool] = UNSET
    total_session_ms: Union[Unset, int] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    state: Union[Unset, BrainstormState] = UNSET
    after_start_ms: Union[Unset, int] = UNSET
    created_tasks_duids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        dartboard_duid = self.dartboard_duid

        subject = self.subject

        ai = self.ai

        total_session_ms = self.total_session_ms

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        after_start_ms = self.after_start_ms

        created_tasks_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.created_tasks_duids, Unset):
            created_tasks_duids = self.created_tasks_duids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
            }
        )
        if dartboard_duid is not UNSET:
            field_dict["dartboardDuid"] = dartboard_duid
        if subject is not UNSET:
            field_dict["subject"] = subject
        if ai is not UNSET:
            field_dict["ai"] = ai
        if total_session_ms is not UNSET:
            field_dict["totalSessionMs"] = total_session_ms
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if state is not UNSET:
            field_dict["state"] = state
        if after_start_ms is not UNSET:
            field_dict["afterStartMs"] = after_start_ms
        if created_tasks_duids is not UNSET:
            field_dict["createdTasksDuids"] = created_tasks_duids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        dartboard_duid = d.pop("dartboardDuid", UNSET)

        subject = d.pop("subject", UNSET)

        ai = d.pop("ai", UNSET)

        total_session_ms = d.pop("totalSessionMs", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _state = d.pop("state", UNSET)
        state: Union[Unset, BrainstormState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = BrainstormState(_state)

        after_start_ms = d.pop("afterStartMs", UNSET)

        created_tasks_duids = cast(list[str], d.pop("createdTasksDuids", UNSET))

        brainstorm_update = cls(
            duid=duid,
            dartboard_duid=dartboard_duid,
            subject=subject,
            ai=ai,
            total_session_ms=total_session_ms,
            started_at=started_at,
            state=state,
            after_start_ms=after_start_ms,
            created_tasks_duids=created_tasks_duids,
        )

        brainstorm_update.additional_properties = d
        return brainstorm_update

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
