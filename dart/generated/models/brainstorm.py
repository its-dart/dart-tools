import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.brainstorm_state import BrainstormState
from ..types import UNSET, Unset

T = TypeVar("T", bound="Brainstorm")


@_attrs_define
class Brainstorm:
    """
    Attributes:
        duid (str):
        dartboard_duid (str):
        subject (str):
        ai (bool):
        total_session_ms (int):
        started_at (datetime.datetime):
        state (BrainstormState): * `Running` - RUNNING
            * `Paused` - PAUSED
            * `Stopped` - STOPPED
        after_start_ms (int):
        created_tasks_duids (List[str]):
        updated_by_client_duid (Union[Unset, None, str]):
    """

    duid: str
    dartboard_duid: str
    subject: str
    ai: bool
    total_session_ms: int
    started_at: datetime.datetime
    state: BrainstormState
    after_start_ms: int
    created_tasks_duids: List[str]
    updated_by_client_duid: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        duid = self.duid
        dartboard_duid = self.dartboard_duid
        subject = self.subject
        ai = self.ai
        total_session_ms = self.total_session_ms
        started_at = self.started_at.isoformat()

        state = self.state.value

        after_start_ms = self.after_start_ms
        created_tasks_duids = self.created_tasks_duids

        updated_by_client_duid = self.updated_by_client_duid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "duid": duid,
                "dartboardDuid": dartboard_duid,
                "subject": subject,
                "ai": ai,
                "totalSessionMs": total_session_ms,
                "startedAt": started_at,
                "state": state,
                "afterStartMs": after_start_ms,
                "createdTasksDuids": created_tasks_duids,
            }
        )
        if updated_by_client_duid is not UNSET:
            field_dict["updatedByClientDuid"] = updated_by_client_duid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        duid = d.pop("duid")

        dartboard_duid = d.pop("dartboardDuid")

        subject = d.pop("subject")

        ai = d.pop("ai")

        total_session_ms = d.pop("totalSessionMs")

        started_at = isoparse(d.pop("startedAt"))

        state = BrainstormState(d.pop("state"))

        after_start_ms = d.pop("afterStartMs")

        created_tasks_duids = cast(List[str], d.pop("createdTasksDuids"))

        updated_by_client_duid = d.pop("updatedByClientDuid", UNSET)

        brainstorm = cls(
            duid=duid,
            dartboard_duid=dartboard_duid,
            subject=subject,
            ai=ai,
            total_session_ms=total_session_ms,
            started_at=started_at,
            state=state,
            after_start_ms=after_start_ms,
            created_tasks_duids=created_tasks_duids,
            updated_by_client_duid=updated_by_client_duid,
        )

        brainstorm.additional_properties = d
        return brainstorm

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
