from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.comment_reaction import CommentReaction
    from ..models.dartboard import Dartboard
    from ..models.doc import Doc
    from ..models.event import Event
    from ..models.event_subscription import EventSubscription
    from ..models.folder import Folder
    from ..models.layout import Layout
    from ..models.relationship import Relationship
    from ..models.relationship_kind import RelationshipKind
    from ..models.space import Space
    from ..models.status import Status
    from ..models.tag import Tag
    from ..models.task import Task
    from ..models.task_attachment import TaskAttachment
    from ..models.task_doc_relationship import TaskDocRelationship
    from ..models.task_link import TaskLink
    from ..models.tenant import Tenant
    from ..models.user import User
    from ..models.user_dartboard_layout import UserDartboardLayout
    from ..models.view import View


T = TypeVar("T", bound="ModelsResponse")


@_attrs_define
class ModelsResponse:
    """This is a helper serializer for OpenAPI schema generation for all available models.
    E.g.:
    {
        "dartboards": [...],
        "layouts": [...],
        "relationships": [...],
        ...
        "views": [...],
    }

        Attributes:
            comments (List['Comment']):
            reactions (List['CommentReaction']):
            dartboards (List['Dartboard']):
            docs (List['Doc']):
            events (List['Event']):
            folders (List['Folder']):
            layouts (List['Layout']):
            event_subscriptions (List['EventSubscription']):
            relationships (List['Relationship']):
            relationship_kinds (List['RelationshipKind']):
            spaces (List['Space']):
            statuses (List['Status']):
            tags (List['Tag']):
            tasks (List['Task']):
            attachments (List['TaskAttachment']):
            task_doc_relationships (List['TaskDocRelationship']):
            links (List['TaskLink']):
            tenants (List['Tenant']):
            users (List['User']):
            user_dartboard_layouts (List['UserDartboardLayout']):
            views (List['View']):
    """

    comments: List["Comment"]
    reactions: List["CommentReaction"]
    dartboards: List["Dartboard"]
    docs: List["Doc"]
    events: List["Event"]
    folders: List["Folder"]
    layouts: List["Layout"]
    event_subscriptions: List["EventSubscription"]
    relationships: List["Relationship"]
    relationship_kinds: List["RelationshipKind"]
    spaces: List["Space"]
    statuses: List["Status"]
    tags: List["Tag"]
    tasks: List["Task"]
    attachments: List["TaskAttachment"]
    task_doc_relationships: List["TaskDocRelationship"]
    links: List["TaskLink"]
    tenants: List["Tenant"]
    users: List["User"]
    user_dartboard_layouts: List["UserDartboardLayout"]
    views: List["View"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments = []
        for comments_item_data in self.comments:
            comments_item = comments_item_data.to_dict()

            comments.append(comments_item)

        reactions = []
        for reactions_item_data in self.reactions:
            reactions_item = reactions_item_data.to_dict()

            reactions.append(reactions_item)

        dartboards = []
        for dartboards_item_data in self.dartboards:
            dartboards_item = dartboards_item_data.to_dict()

            dartboards.append(dartboards_item)

        docs = []
        for docs_item_data in self.docs:
            docs_item = docs_item_data.to_dict()

            docs.append(docs_item)

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()

            events.append(events_item)

        folders = []
        for folders_item_data in self.folders:
            folders_item = folders_item_data.to_dict()

            folders.append(folders_item)

        layouts = []
        for layouts_item_data in self.layouts:
            layouts_item = layouts_item_data.to_dict()

            layouts.append(layouts_item)

        event_subscriptions = []
        for event_subscriptions_item_data in self.event_subscriptions:
            event_subscriptions_item = event_subscriptions_item_data.to_dict()

            event_subscriptions.append(event_subscriptions_item)

        relationships = []
        for relationships_item_data in self.relationships:
            relationships_item = relationships_item_data.to_dict()

            relationships.append(relationships_item)

        relationship_kinds = []
        for relationship_kinds_item_data in self.relationship_kinds:
            relationship_kinds_item = relationship_kinds_item_data.to_dict()

            relationship_kinds.append(relationship_kinds_item)

        spaces = []
        for spaces_item_data in self.spaces:
            spaces_item = spaces_item_data.to_dict()

            spaces.append(spaces_item)

        statuses = []
        for statuses_item_data in self.statuses:
            statuses_item = statuses_item_data.to_dict()

            statuses.append(statuses_item)

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()

            tags.append(tags_item)

        tasks = []
        for tasks_item_data in self.tasks:
            tasks_item = tasks_item_data.to_dict()

            tasks.append(tasks_item)

        attachments = []
        for attachments_item_data in self.attachments:
            attachments_item = attachments_item_data.to_dict()

            attachments.append(attachments_item)

        task_doc_relationships = []
        for task_doc_relationships_item_data in self.task_doc_relationships:
            task_doc_relationships_item = task_doc_relationships_item_data.to_dict()

            task_doc_relationships.append(task_doc_relationships_item)

        links = []
        for links_item_data in self.links:
            links_item = links_item_data.to_dict()

            links.append(links_item)

        tenants = []
        for tenants_item_data in self.tenants:
            tenants_item = tenants_item_data.to_dict()

            tenants.append(tenants_item)

        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        user_dartboard_layouts = []
        for user_dartboard_layouts_item_data in self.user_dartboard_layouts:
            user_dartboard_layouts_item = user_dartboard_layouts_item_data.to_dict()

            user_dartboard_layouts.append(user_dartboard_layouts_item)

        views = []
        for views_item_data in self.views:
            views_item = views_item_data.to_dict()

            views.append(views_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "comments": comments,
                "reactions": reactions,
                "dartboards": dartboards,
                "docs": docs,
                "events": events,
                "folders": folders,
                "layouts": layouts,
                "eventSubscriptions": event_subscriptions,
                "relationships": relationships,
                "relationshipKinds": relationship_kinds,
                "spaces": spaces,
                "statuses": statuses,
                "tags": tags,
                "tasks": tasks,
                "attachments": attachments,
                "taskDocRelationships": task_doc_relationships,
                "links": links,
                "tenants": tenants,
                "users": users,
                "userDartboardLayouts": user_dartboard_layouts,
                "views": views,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comment import Comment
        from ..models.comment_reaction import CommentReaction
        from ..models.dartboard import Dartboard
        from ..models.doc import Doc
        from ..models.event import Event
        from ..models.event_subscription import EventSubscription
        from ..models.folder import Folder
        from ..models.layout import Layout
        from ..models.relationship import Relationship
        from ..models.relationship_kind import RelationshipKind
        from ..models.space import Space
        from ..models.status import Status
        from ..models.tag import Tag
        from ..models.task import Task
        from ..models.task_attachment import TaskAttachment
        from ..models.task_doc_relationship import TaskDocRelationship
        from ..models.task_link import TaskLink
        from ..models.tenant import Tenant
        from ..models.user import User
        from ..models.user_dartboard_layout import UserDartboardLayout
        from ..models.view import View

        d = src_dict.copy()
        comments = []
        _comments = d.pop("comments")
        for comments_item_data in _comments:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        reactions = []
        _reactions = d.pop("reactions")
        for reactions_item_data in _reactions:
            reactions_item = CommentReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        dartboards = []
        _dartboards = d.pop("dartboards")
        for dartboards_item_data in _dartboards:
            dartboards_item = Dartboard.from_dict(dartboards_item_data)

            dartboards.append(dartboards_item)

        docs = []
        _docs = d.pop("docs")
        for docs_item_data in _docs:
            docs_item = Doc.from_dict(docs_item_data)

            docs.append(docs_item)

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        folders = []
        _folders = d.pop("folders")
        for folders_item_data in _folders:
            folders_item = Folder.from_dict(folders_item_data)

            folders.append(folders_item)

        layouts = []
        _layouts = d.pop("layouts")
        for layouts_item_data in _layouts:
            layouts_item = Layout.from_dict(layouts_item_data)

            layouts.append(layouts_item)

        event_subscriptions = []
        _event_subscriptions = d.pop("eventSubscriptions")
        for event_subscriptions_item_data in _event_subscriptions:
            event_subscriptions_item = EventSubscription.from_dict(event_subscriptions_item_data)

            event_subscriptions.append(event_subscriptions_item)

        relationships = []
        _relationships = d.pop("relationships")
        for relationships_item_data in _relationships:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        relationship_kinds = []
        _relationship_kinds = d.pop("relationshipKinds")
        for relationship_kinds_item_data in _relationship_kinds:
            relationship_kinds_item = RelationshipKind.from_dict(relationship_kinds_item_data)

            relationship_kinds.append(relationship_kinds_item)

        spaces = []
        _spaces = d.pop("spaces")
        for spaces_item_data in _spaces:
            spaces_item = Space.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        statuses = []
        _statuses = d.pop("statuses")
        for statuses_item_data in _statuses:
            statuses_item = Status.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in _tags:
            tags_item = Tag.from_dict(tags_item_data)

            tags.append(tags_item)

        tasks = []
        _tasks = d.pop("tasks")
        for tasks_item_data in _tasks:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        attachments = []
        _attachments = d.pop("attachments")
        for attachments_item_data in _attachments:
            attachments_item = TaskAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        task_doc_relationships = []
        _task_doc_relationships = d.pop("taskDocRelationships")
        for task_doc_relationships_item_data in _task_doc_relationships:
            task_doc_relationships_item = TaskDocRelationship.from_dict(task_doc_relationships_item_data)

            task_doc_relationships.append(task_doc_relationships_item)

        links = []
        _links = d.pop("links")
        for links_item_data in _links:
            links_item = TaskLink.from_dict(links_item_data)

            links.append(links_item)

        tenants = []
        _tenants = d.pop("tenants")
        for tenants_item_data in _tenants:
            tenants_item = Tenant.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        user_dartboard_layouts = []
        _user_dartboard_layouts = d.pop("userDartboardLayouts")
        for user_dartboard_layouts_item_data in _user_dartboard_layouts:
            user_dartboard_layouts_item = UserDartboardLayout.from_dict(user_dartboard_layouts_item_data)

            user_dartboard_layouts.append(user_dartboard_layouts_item)

        views = []
        _views = d.pop("views")
        for views_item_data in _views:
            views_item = View.from_dict(views_item_data)

            views.append(views_item)

        models_response = cls(
            comments=comments,
            reactions=reactions,
            dartboards=dartboards,
            docs=docs,
            events=events,
            folders=folders,
            layouts=layouts,
            event_subscriptions=event_subscriptions,
            relationships=relationships,
            relationship_kinds=relationship_kinds,
            spaces=spaces,
            statuses=statuses,
            tags=tags,
            tasks=tasks,
            attachments=attachments,
            task_doc_relationships=task_doc_relationships,
            links=links,
            tenants=tenants,
            users=users,
            user_dartboard_layouts=user_dartboard_layouts,
            views=views,
        )

        models_response.additional_properties = d
        return models_response

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
