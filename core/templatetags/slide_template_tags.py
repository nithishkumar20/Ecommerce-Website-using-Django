from django import template
from django.utils.safestring import mark_safe

from core.models import Slide

register = template.Library()


@register.simple_tag
def slides():
    items = Slide.objects.filter(is_active=True).order_by('pk')
    items_div = ""
    for i in items:
        items_div += """<div class="item-slick1" style="background-image: url('media/{}');">
					<div class="container h-full">
						<div class="flex-col-l-m h-full p-t-100 p-b-30 respon5">
							<div class="layer-slick1 animated visible-false" data-appear="fadeInDown" data-delay="0">
								<span class="ltext-101 cl2 respon2">
									{}
								</span>
							</div>
								
							<div class="layer-slick1 animated visible-false" data-appear="fadeInUp" data-delay="800">
								<h2 class="ltext-201 cl2 p-t-19 p-b-43 respon1">
									{}
								</h2>
							</div>
								
							<div class="layer-slick1 animated visible-false" data-appear="zoomIn" data-delay="1600">
								<a href="{}" class="flex-c-m stext-101 cl0 size-101 bg1 bor1 hov-btn1 p-lr-15 trans-04">
									Shop Now
								</a>
							</div>
						</div>
					</div>
				</div>""".format(
            i.image, i.caption1, i.caption2, i.link)
    return mark_safe(items_div)
