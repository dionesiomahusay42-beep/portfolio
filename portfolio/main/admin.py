from django.contrib import admin
from django.utils.html import format_html
from .models import SiteProfile, Skill, Project, Education, ContactMessage

admin.site.site_header  = "Dionesio Mahusay | Portfolio Admin"
admin.site.site_title   = "Portfolio Admin"
admin.site.index_title  = "Edit Your Portfolio Content"


@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'tagline', 'short_bio')
        }),
        ('About Section', {
            'fields': ('about', 'career_goals')
        }),
        ('Contact & Social Links', {
            'fields': ('email', 'github', 'linkedin', 'twitter')
        }),
    )

    def has_add_permission(self, request):
        return not SiteProfile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'category', 'proficiency_bar', 'order')
    list_editable = ('order',)
    list_filter   = ('category',)
    search_fields = ('name',)

    def proficiency_bar(self, obj):
        return format_html(
            '<div style="width:150px;background:#e5e7eb;border-radius:4px;height:8px;">'
            '<div style="width:{}%;background:#2563eb;border-radius:4px;height:8px;"></div>'
            '</div> {}%',
            obj.proficiency, obj.proficiency
        )
    proficiency_bar.short_description = 'Proficiency'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('emoji', 'title', 'featured', 'order')
    list_editable = ('featured', 'order')
    search_fields = ('title', 'description')
    list_filter   = ('featured',)
    fieldsets = (
        ('Project Info', {
            'fields': ('emoji', 'title', 'description')
        }),
        ('Technologies', {
            'fields': ('tech',),
            'description': 'Enter comma-separated: Java, MySQL, NetBeans'
        }),
        ('Links', {
            'fields': ('github_url', 'live_url')
        }),
        ('Display', {
            'fields': ('featured', 'order')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('school', 'degree', 'year', 'order')
    list_editable = ('order',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter     = ('is_read', 'created_at')
    search_fields   = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    list_editable   = ('is_read',)

    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"