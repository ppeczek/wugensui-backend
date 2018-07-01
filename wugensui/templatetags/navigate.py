from django.template import Library
from django.urls import reverse


register = Library()


@register.inclusion_tag('templatetags/navigate/pagination.html')
def pagination(is_paginated=False, paginator=None, page_obj=None):
    return {
        'is_paginated': is_paginated,
        'paginator': paginator,
        'page_obj': page_obj
    }


@register.inclusion_tag('templatetags/navigate/navbar.html', takes_context=True)
def navbar(context):
    current_path = context['request'].get_full_path()
    home_url = reverse('home')
    videos_url = reverse('video-list')
    item_list = [
        {
            'active': home_url == current_path,
            'title': 'Home',
            'url': home_url
        },
        {
            'active': videos_url in current_path,
            'title': 'Videos',
            'url': videos_url
        }
    ]
    context.update({
        'item_list': item_list
    })
    return context
