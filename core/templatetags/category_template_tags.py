from django import template
from django.utils.safestring import mark_safe

from core.models import Category

register = template.Library()


@register.simple_tag
def categories():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li = ""
    for i in items:
        items_li += """<button class="stext-106 cl6 hov1 bor3 trans-04 m-r-32 m-tb-5" data-filter=".{}">
                            {}
                    </button>""".format(i.slug, i.title)
    return mark_safe(items_li)


@register.simple_tag
def categories_filter():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li = ""
    for i in items:
        items_li += """<a href="/category/{}"
                        class="flex-c-m stext-107 cl6 size-301 bor7 p-lr-15 hov-tag1 trans-04 m-r-5 m-b-5">
                        {}</a>""".format(i.slug, i.title)
    return mark_safe(items_li)


@register.simple_tag
def categories_list():
    items = Category.objects.all()
    items_li_a = ""
    for i in items:
        items_li_a += """<div class="col-md-6 col-xl-4 p-b-30 m-lr-auto">
                    <!-- Block1 -->
                    <div class="block1 wrap-pic-w">
                        <img src="{}" alt="IMG-BANNER" height="200">

                        <a href="/category/{}"
                           class="block1-txt ab-t-l s-full flex-col-l-sb p-lr-38 p-tb-34 trans-03 respon3">
                            <div class="block1-txt-child1 flex-col-l">
								<span class="block1-name ltext-102 trans-04 p-b-8">
									{}
								</span>

                                <span class="block1-info stext-102 trans-04">
									Spring 2020
								</span>
                            </div>

                            <div class="block1-txt-child2 p-b-4 trans-05">
                                <a href="" class="block1-link stext-101 cl0 trans-09">
                                    Shop Now
                                </a>
                            </div>
                        </a>
                    </div>
                </div>""".format(i.image.url, i.slug, i.title)
    return mark_safe(items_li_a)


@register.simple_tag
def categories_div():
    """
    section banner
    :return:
    """
    items = Category.objects.filter(is_active=True).order_by('title')
    items_div = ""
    item_div_list = ""
    for i, j in enumerate(items):
        if not i % 2:
            items_div += """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.image, j.slug, j.title)
        else:
            items_div_ = """<div class="block1 hov-img-zoom pos-relative m-b-30"><img src="/media/{}" alt="IMG-BENNER"><div class="block1-wrapbtn w-size2"><a href="/category/{}" class="flex-c-m size2 m-text2 bg3 hov1 trans-0-4">{}</a></div></div>""".format(
                j.image, j.slug, j.title)
            item_div_list += """<div class="col-sm-10 col-md-8 col-lg-4 m-l-r-auto">""" + items_div + items_div_ + """</div>"""
            items_div = ""

    return mark_safe(item_div_list)
