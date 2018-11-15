# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522989287.663971
_enable_loop = True
_template_filename = u'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = u'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_navigation_links', 'html_tags', 'html_stylesheets', 'html_translations', 'html_title', 'late_load_js', 'html_sourcelink', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        description = context.get('description', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html>\n<html\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer(u"prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer(u'og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer(u'article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer(u'fb: http://ogp.me/ns/fb# ')
            __M_writer(u"'")
        if is_rtl:
            __M_writer(u'dir="rtl" ')
        __M_writer(u'lang="')
        __M_writer(unicode(lang))
        __M_writer(u'">\n    <head>\n    <meta charset="utf-8">\n')
        if description:
            __M_writer(u'    <meta name="description" content="')
            __M_writer(unicode(description))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="viewport" content="width=device-width">\n    <title>')
        __M_writer(striphtml(unicode(title)))
        __M_writer(u' | ')
        __M_writer(striphtml(unicode(blog_title)))
        __M_writer(u'</title>\n\n    ')
        __M_writer(unicode(html_stylesheets()))
        __M_writer(u'\n    ')
        __M_writer(unicode(html_feedlinks()))
        __M_writer(u'\n')
        if permalink:
            __M_writer(u'      <link rel="canonical" href="')
            __M_writer(unicode(abs_link(permalink)))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer(u'            <link rel="')
                __M_writer(unicode(name))
                __M_writer(u'" href="')
                __M_writer(unicode(file))
                __M_writer(u'" sizes="')
                __M_writer(unicode(size))
                __M_writer(u'"/>\n')
        __M_writer(u'\n')
        if comment_system == 'facebook':
            __M_writer(u'        <meta property="fb:app_id" content="')
            __M_writer(unicode(comment_system_id))
            __M_writer(u'">\n')
        __M_writer(u'\n')
        if use_cdn:
            __M_writer(u'        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer(u'        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\n')
        __M_writer(u'\n    ')
        __M_writer(unicode(extra_head_data))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        for url, text, icon in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(url))
                __M_writer(u'" title="')
                __M_writer(unicode(text))
                __M_writer(u'"><i class="')
                __M_writer(unicode(icon))
                __M_writer(u'"></i></a></li>\n')
            else:
                __M_writer(u'            <li><a href="')
                __M_writer(unicode(url))
                __M_writer(u'" title="')
                __M_writer(unicode(text))
                __M_writer(u'"><i class="')
                __M_writer(unicode(icon))
                __M_writer(u'"></i></a></li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if post.tags:
            __M_writer(u'        <div itemprop="keywords" class="tags">\n        <ul>\n        ')
            __M_writer(unicode(messages("Tags")))
            __M_writer(u'&nbsp;:&nbsp;\n')
            for tag in post.tags:
                __M_writer(u'           <li><a class="tag p-category" href="')
                __M_writer(unicode(_link('tag', tag)))
                __M_writer(u'" rel="tag">')
                __M_writer(unicode(tag))
                __M_writer(u'</a></li>\n')
            __M_writer(u'        </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        notes = context.get('notes', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <link href=\'//fonts.googleapis.com/css?family=Bitter:400,400italic,700\' rel=\'stylesheet\' type=\'text/css\'>\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer(u'            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            if use_cdn:
                __M_writer(u"            <link href='//fonts.googleapis.com/css?family=Bitter:400,400italic,700' rel='stylesheet' type='text/css'>\n")
            else:
                __M_writer(u'            <link href="/assets/css/bitter.css" rel="stylesheet" type="text/css">\n')
            __M_writer(u'        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer(u'            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(u'        ')
            __M_writer(unicode(notes.css()))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer(u'                <a href="')
                    __M_writer(unicode(post.permalink(langname)))
                    __M_writer(u'" rel="alternate" hreflang="')
                    __M_writer(unicode(langname))
                    __M_writer(u'">\n                ')
                    __M_writer(unicode(messages("LANGUAGE", langname)))
                    __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if title and not post.meta('hidetitle'):
            __M_writer(u'    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(unicode(title)))
            __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if use_bundles:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\n')
        else:
            if use_cdn:
                __M_writer(u'            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\n')
            else:
                __M_writer(u'            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\n')
        __M_writer(u'    ')
        __M_writer(unicode(social_buttons_code))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if show_sourcelink:
            __M_writer(u'        &nbsp;&nbsp;|&nbsp;&nbsp;\n        <a href="')
            __M_writer(unicode(post.source_link()))
            __M_writer(u'" id="sourcelink">')
            __M_writer(unicode(messages("Source")))
            __M_writer(u'</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        generate_rss = context.get('generate_rss', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if rss_link:
            __M_writer(u'        ')
            __M_writer(unicode(rss_link))
            __M_writer(u'\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer(u'                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(unicode(language))
                    __M_writer(u')" href="')
                    __M_writer(unicode(_link('rss', None, language)))
                    __M_writer(u'">\n')
            else:
                __M_writer(u'            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(unicode(_link('rss', None)))
                __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 57, "22": 85, "23": 105, "24": 119, "25": 129, "26": 143, "27": 150, "28": 161, "29": 168, "35": 3, "58": 3, "59": 7, "60": 8, "61": 9, "62": 10, "63": 12, "64": 13, "65": 15, "66": 16, "67": 18, "68": 21, "69": 22, "70": 25, "71": 25, "72": 25, "73": 28, "74": 29, "75": 29, "76": 29, "77": 31, "78": 32, "79": 32, "80": 32, "81": 32, "82": 34, "83": 34, "84": 35, "85": 35, "86": 36, "87": 37, "88": 37, "89": 37, "90": 39, "91": 40, "92": 41, "93": 42, "94": 42, "95": 42, "96": 42, "97": 42, "98": 42, "99": 42, "100": 45, "101": 46, "102": 47, "103": 47, "104": 47, "105": 49, "106": 50, "107": 51, "108": 52, "109": 53, "110": 55, "111": 56, "112": 56, "118": 121, "126": 121, "127": 122, "128": 123, "129": 124, "130": 124, "131": 124, "132": 124, "133": 124, "134": 124, "135": 124, "136": 125, "137": 126, "138": 126, "139": 126, "140": 126, "141": 126, "142": 126, "143": 126, "149": 132, "155": 132, "156": 133, "157": 134, "158": 136, "159": 136, "160": 137, "161": 138, "162": 138, "163": 138, "164": 138, "165": 138, "166": 140, "172": 59, "182": 59, "183": 60, "184": 61, "185": 62, "186": 64, "187": 65, "188": 67, "189": 68, "190": 69, "191": 70, "192": 71, "193": 73, "194": 76, "195": 77, "196": 80, "197": 81, "198": 81, "199": 81, "200": 82, "201": 83, "202": 83, "203": 83, "209": 152, "217": 152, "218": 153, "219": 154, "220": 155, "221": 156, "222": 156, "223": 156, "224": 156, "225": 156, "226": 157, "227": 157, "233": 146, "239": 146, "240": 147, "241": 148, "242": 148, "243": 148, "249": 87, "256": 87, "257": 88, "258": 89, "259": 90, "260": 92, "261": 93, "262": 95, "263": 96, "264": 97, "265": 99, "266": 100, "267": 104, "268": 104, "269": 104, "275": 163, "282": 163, "283": 164, "284": 165, "285": 166, "286": 166, "287": 166, "288": 166, "294": 107, "303": 107, "304": 108, "305": 109, "306": 109, "307": 109, "308": 110, "309": 111, "310": 112, "311": 113, "312": 113, "313": 113, "314": 113, "315": 113, "316": 115, "317": 116, "318": 116, "319": 116, "325": 319}, "uri": "arusahni_helper.tmpl", "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
