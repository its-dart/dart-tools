import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.brainstorm_state import BrainstormState
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrainstormCreate")


@_attrs_define
class BrainstormCreate:
    """
    Attributes:
        duid (str):
        dartboard_duid (str):
        subject (str):
        ai (bool):
        started_at (datetime.datetime):
        state (BrainstormState): * `Running` - RUNNING
            * `Paused` - PAUSED
            * `Stopped` - STOPPED
        total_session_ms (Union[Unset, int]):
        after_start_ms (Union[Unset, int]):
        created_tasks_duids (Union[Unset, list[str]]):
    """

    duid: str
    dartboard_duid: str
    subject: str
    ai: bool
    started_at: datetime.datetime
    state: BrainstormState
    total_session_ms: Union[Unset, int] = UNSET
    after_start_ms: Union[Unset, int] = UNSET
    created_tasks_duids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        duid = self.duid

        dartboard_duid = self.dartboard_duid

        subject = self.subject

        ai = self.ai

        started_at = self.started_at.isoformat()

        state = self.state.value

        total_session_ms = self.total_session_ms

        after_start_ms = self.after_start_ms

        created_tasks_duids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.created_tasks_duids, Unset):
            created_tasks_duids = self.created_tasks_duids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "dartboardDuid": dartboard_duid,
                "subject": subject,
                "ai": ai,
                "startedAt": started_at,
                "state": state,
            }
        )
        if total_session_ms is not UNSET:
            field_dict["totalSessionMs"] = total_session_ms
        if after_start_ms is not UNSET:
            field_dict["afterStartMs"] = after_start_ms
        if created_tasks_duids is not UNSET:
            field_dict["createdTasksDuids"] = created_tasks_duids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        dartboard_duid = d.pop("dartboardDuid")

        subject = d.pop("subject")

        ai = d.pop("ai")

        started_at = isoparse(d.pop("startedAt"))

        state = BrainstormState(d.pop("state"))

        total_session_ms = d.pop("totalSessionMs", UNSET)

        after_start_ms = d.pop("afterStartMs", UNSET)

        created_tasks_duids = cast(list[str], d.pop("createdTasksDuids", UNSET))

        brainstorm_create = cls(
            duid=duid,
            dartboard_duid=dartboard_duid,
            subject=subject,
            ai=ai,
            started_at=started_at,
            state=state,
            total_session_ms=total_session_ms,
            after_start_ms=after_start_ms,
            created_tasks_duids=created_tasks_duids,
        )

        brainstorm_create.additional_properties = d
        return brainstorm_create

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
