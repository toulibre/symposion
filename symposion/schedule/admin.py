from django.contrib import admin

from symposion.schedule.models import Schedule, Day, Room, SlotKind, Slot, SlotRoom, Presentation, Session, SessionRole


admin.site.register(Schedule)
admin.site.register(Day)
admin.site.register(Room)
admin.site.register(SlotKind)
admin.site.register(
    Slot,
    list_display=("day", "content", "start", "end", "kind", "rooms"),
    list_filter=("day",),
    search_fields = ['content_ptr']
)
admin.site.register(
    SlotRoom,
    list_display=("slot", "room"),
    list_filter=("room",),
)
admin.site.register(Session)
admin.site.register(SessionRole)
admin.site.register(
    Presentation,
    list_filter=("section",),
)
