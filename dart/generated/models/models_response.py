from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment import Comment
    from ..models.comment_reaction import CommentReaction
    from ..models.dartboard import Dartboard
    from ..models.doc import Doc
    from ..models.event import Event
    from ..models.event_subscription import EventSubscription
    from ..models.folder import Folder
    from ..models.layout import Layout
    from ..models.option import Option
    from ..models.property_ import Property
    from ..models.relationship import Relationship
    from ..models.relationship_kind import RelationshipKind
    from ..models.space import Space
    from ..models.status import Status
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
            comments (Union[Unset, List['Comment']]):
            reactions (Union[Unset, List['CommentReaction']]):
            dartboards (Union[Unset, List['Dartboard']]):
            docs (Union[Unset, List['Doc']]):
            events (Union[Unset, List['Event']]):
            folders (Union[Unset, List['Folder']]):
            layouts (Union[Unset, List['Layout']]):
            event_subscriptions (Union[Unset, List['EventSubscription']]):
            options (Union[Unset, List['Option']]):
            properties (Union[Unset, List['Property']]):
            relationships (Union[Unset, List['Relationship']]):
            relationship_kinds (Union[Unset, List['RelationshipKind']]):
            spaces (Union[Unset, List['Space']]):
            statuses (Union[Unset, List['Status']]):
            tasks (Union[Unset, List['Task']]):
            attachments (Union[Unset, List['TaskAttachment']]):
            task_doc_relationships (Union[Unset, List['TaskDocRelationship']]):
            links (Union[Unset, List['TaskLink']]):
            tenants (Union[Unset, List['Tenant']]):
            users (Union[Unset, List['User']]):
            user_dartboard_layouts (Union[Unset, List['UserDartboardLayout']]):
            views (Union[Unset, List['View']]):
    """

    comments: Union[Unset, List["Comment"]] = UNSET
    reactions: Union[Unset, List["CommentReaction"]] = UNSET
    dartboards: Union[Unset, List["Dartboard"]] = UNSET
    docs: Union[Unset, List["Doc"]] = UNSET
    events: Union[Unset, List["Event"]] = UNSET
    folders: Union[Unset, List["Folder"]] = UNSET
    layouts: Union[Unset, List["Layout"]] = UNSET
    event_subscriptions: Union[Unset, List["EventSubscription"]] = UNSET
    options: Union[Unset, List["Option"]] = UNSET
    properties: Union[Unset, List["Property"]] = UNSET
    relationships: Union[Unset, List["Relationship"]] = UNSET
    relationship_kinds: Union[Unset, List["RelationshipKind"]] = UNSET
    spaces: Union[Unset, List["Space"]] = UNSET
    statuses: Union[Unset, List["Status"]] = UNSET
    tasks: Union[Unset, List["Task"]] = UNSET
    attachments: Union[Unset, List["TaskAttachment"]] = UNSET
    task_doc_relationships: Union[Unset, List["TaskDocRelationship"]] = UNSET
    links: Union[Unset, List["TaskLink"]] = UNSET
    tenants: Union[Unset, List["Tenant"]] = UNSET
    users: Union[Unset, List["User"]] = UNSET
    user_dartboard_layouts: Union[Unset, List["UserDartboardLayout"]] = UNSET
    views: Union[Unset, List["View"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comments, Unset):
            comments = []
            for comments_item_data in self.comments:
                comments_item = comments_item_data.to_dict()

                comments.append(comments_item)

        reactions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()

                reactions.append(reactions_item)

        dartboards: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.dartboards, Unset):
            dartboards = []
            for dartboards_item_data in self.dartboards:
                dartboards_item = dartboards_item_data.to_dict()

                dartboards.append(dartboards_item)

        docs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.docs, Unset):
            docs = []
            for docs_item_data in self.docs:
                docs_item = docs_item_data.to_dict()

                docs.append(docs_item)

        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()

                events.append(events_item)

        folders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.folders, Unset):
            folders = []
            for folders_item_data in self.folders:
                folders_item = folders_item_data.to_dict()

                folders.append(folders_item)

        layouts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.layouts, Unset):
            layouts = []
            for layouts_item_data in self.layouts:
                layouts_item = layouts_item_data.to_dict()

                layouts.append(layouts_item)

        event_subscriptions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.event_subscriptions, Unset):
            event_subscriptions = []
            for event_subscriptions_item_data in self.event_subscriptions:
                event_subscriptions_item = event_subscriptions_item_data.to_dict()

                event_subscriptions.append(event_subscriptions_item)

        options: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()

                options.append(options_item)

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = []
            for relationships_item_data in self.relationships:
                relationships_item = relationships_item_data.to_dict()

                relationships.append(relationships_item)

        relationship_kinds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.relationship_kinds, Unset):
            relationship_kinds = []
            for relationship_kinds_item_data in self.relationship_kinds:
                relationship_kinds_item = relationship_kinds_item_data.to_dict()

                relationship_kinds.append(relationship_kinds_item)

        spaces: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spaces, Unset):
            spaces = []
            for spaces_item_data in self.spaces:
                spaces_item = spaces_item_data.to_dict()

                spaces.append(spaces_item)

        statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.statuses, Unset):
            statuses = []
            for statuses_item_data in self.statuses:
                statuses_item = statuses_item_data.to_dict()

                statuses.append(statuses_item)

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        task_doc_relationships: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.task_doc_relationships, Unset):
            task_doc_relationships = []
            for task_doc_relationships_item_data in self.task_doc_relationships:
                task_doc_relationships_item = task_doc_relationships_item_data.to_dict()

                task_doc_relationships.append(task_doc_relationships_item)

        links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()

                links.append(links_item)

        tenants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tenants, Unset):
            tenants = []
            for tenants_item_data in self.tenants:
                tenants_item = tenants_item_data.to_dict()

                tenants.append(tenants_item)

        users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()

                users.append(users_item)

        user_dartboard_layouts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_dartboard_layouts, Unset):
            user_dartboard_layouts = []
            for user_dartboard_layouts_item_data in self.user_dartboard_layouts:
                user_dartboard_layouts_item = user_dartboard_layouts_item_data.to_dict()

                user_dartboard_layouts.append(user_dartboard_layouts_item)

        views: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()

                views.append(views_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comments is not UNSET:
            field_dict["comments"] = comments
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if dartboards is not UNSET:
            field_dict["dartboards"] = dartboards
        if docs is not UNSET:
            field_dict["docs"] = docs
        if events is not UNSET:
            field_dict["events"] = events
        if folders is not UNSET:
            field_dict["folders"] = folders
        if layouts is not UNSET:
            field_dict["layouts"] = layouts
        if event_subscriptions is not UNSET:
            field_dict["eventSubscriptions"] = event_subscriptions
        if options is not UNSET:
            field_dict["options"] = options
        if properties is not UNSET:
            field_dict["properties"] = properties
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if relationship_kinds is not UNSET:
            field_dict["relationshipKinds"] = relationship_kinds
        if spaces is not UNSET:
            field_dict["spaces"] = spaces
        if statuses is not UNSET:
            field_dict["statuses"] = statuses
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if task_doc_relationships is not UNSET:
            field_dict["taskDocRelationships"] = task_doc_relationships
        if links is not UNSET:
            field_dict["links"] = links
        if tenants is not UNSET:
            field_dict["tenants"] = tenants
        if users is not UNSET:
            field_dict["users"] = users
        if user_dartboard_layouts is not UNSET:
            field_dict["userDartboardLayouts"] = user_dartboard_layouts
        if views is not UNSET:
            field_dict["views"] = views

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
        from ..models.option import Option
        from ..models.property_ import Property
        from ..models.relationship import Relationship
        from ..models.relationship_kind import RelationshipKind
        from ..models.space import Space
        from ..models.status import Status
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
        _comments = d.pop("comments", UNSET)
        for comments_item_data in _comments or []:
            comments_item = Comment.from_dict(comments_item_data)

            comments.append(comments_item)

        reactions = []
        _reactions = d.pop("reactions", UNSET)
        for reactions_item_data in _reactions or []:
            reactions_item = CommentReaction.from_dict(reactions_item_data)

            reactions.append(reactions_item)

        dartboards = []
        _dartboards = d.pop("dartboards", UNSET)
        for dartboards_item_data in _dartboards or []:
            dartboards_item = Dartboard.from_dict(dartboards_item_data)

            dartboards.append(dartboards_item)

        docs = []
        _docs = d.pop("docs", UNSET)
        for docs_item_data in _docs or []:
            docs_item = Doc.from_dict(docs_item_data)

            docs.append(docs_item)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        folders = []
        _folders = d.pop("folders", UNSET)
        for folders_item_data in _folders or []:
            folders_item = Folder.from_dict(folders_item_data)

            folders.append(folders_item)

        layouts = []
        _layouts = d.pop("layouts", UNSET)
        for layouts_item_data in _layouts or []:
            layouts_item = Layout.from_dict(layouts_item_data)

            layouts.append(layouts_item)

        event_subscriptions = []
        _event_subscriptions = d.pop("eventSubscriptions", UNSET)
        for event_subscriptions_item_data in _event_subscriptions or []:
            event_subscriptions_item = EventSubscription.from_dict(event_subscriptions_item_data)

            event_subscriptions.append(event_subscriptions_item)

        options = []
        _options = d.pop("options", UNSET)
        for options_item_data in _options or []:
            options_item = Option.from_dict(options_item_data)

            options.append(options_item)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Property.from_dict(properties_item_data)

            properties.append(properties_item)

        relationships = []
        _relationships = d.pop("relationships", UNSET)
        for relationships_item_data in _relationships or []:
            relationships_item = Relationship.from_dict(relationships_item_data)

            relationships.append(relationships_item)

        relationship_kinds = []
        _relationship_kinds = d.pop("relationshipKinds", UNSET)
        for relationship_kinds_item_data in _relationship_kinds or []:
            relationship_kinds_item = RelationshipKind.from_dict(relationship_kinds_item_data)

            relationship_kinds.append(relationship_kinds_item)

        spaces = []
        _spaces = d.pop("spaces", UNSET)
        for spaces_item_data in _spaces or []:
            spaces_item = Space.from_dict(spaces_item_data)

            spaces.append(spaces_item)

        statuses = []
        _statuses = d.pop("statuses", UNSET)
        for statuses_item_data in _statuses or []:
            statuses_item = Status.from_dict(statuses_item_data)

            statuses.append(statuses_item)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = TaskAttachment.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        task_doc_relationships = []
        _task_doc_relationships = d.pop("taskDocRelationships", UNSET)
        for task_doc_relationships_item_data in _task_doc_relationships or []:
            task_doc_relationships_item = TaskDocRelationship.from_dict(task_doc_relationships_item_data)

            task_doc_relationships.append(task_doc_relationships_item)

        links = []
        _links = d.pop("links", UNSET)
        for links_item_data in _links or []:
            links_item = TaskLink.from_dict(links_item_data)

            links.append(links_item)

        tenants = []
        _tenants = d.pop("tenants", UNSET)
        for tenants_item_data in _tenants or []:
            tenants_item = Tenant.from_dict(tenants_item_data)

            tenants.append(tenants_item)

        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in _users or []:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        user_dartboard_layouts = []
        _user_dartboard_layouts = d.pop("userDartboardLayouts", UNSET)
        for user_dartboard_layouts_item_data in _user_dartboard_layouts or []:
            user_dartboard_layouts_item = UserDartboardLayout.from_dict(user_dartboard_layouts_item_data)

            user_dartboard_layouts.append(user_dartboard_layouts_item)

        views = []
        _views = d.pop("views", UNSET)
        for views_item_data in _views or []:
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
            options=options,
            properties=properties,
            relationships=relationships,
            relationship_kinds=relationship_kinds,
            spaces=spaces,
            statuses=statuses,
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
