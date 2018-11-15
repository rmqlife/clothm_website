# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522989288.01175
_enable_loop = True
_template_filename = u'themes/zen/templates/post.tmpl'
_template_uri = u'post.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content', u'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'arusahni', context._clean_inheritance_tokens(), templateuri=u'arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'arusahni')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'helper')] = ns

    ns = runtime.TemplateNamespace(u'comments', context._clean_inheritance_tokens(), templateuri=u'comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'arusahni')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer(u'\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'arusahni')._populate(_import_ns, [u'*'])
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    <div class="post">\n    ')
        __M_writer(unicode(arusahni.html_title()))
        __M_writer(u'\n        <div class="meta">\n            <div class="authordate">\n                <time class="timeago" datetime="')
        __M_writer(unicode(post.date.isoformat()))
        __M_writer(u'">')
        __M_writer(unicode(post.formatted_date(date_format)))
        __M_writer(u'</time>\n            ')
        __M_writer(unicode(arusahni.html_translations(post)))
        __M_writer(u'\n            ')
        __M_writer(unicode(arusahni.html_sourcelink()))
        __M_writer(u'\n            </div>\n            ')
        __M_writer(unicode(arusahni.html_tags(post)))
        __M_writer(u'\n        </div>\n        <div class="body">\n            ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n        </div>\n        ')
        __M_writer(unicode(helper.html_pager(post)))
        __M_writer(u'\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer(u'            ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer(u'\n')
        __M_writer(u'        ')
        __M_writer(unicode(helper.mathjax_script(post)))
        __M_writer(u'\n    </div>\n')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'arusahni')._populate(_import_ns, [u'*'])
        def extra_head():
            return render_extra_head(context)
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.extra_head()))
        __M_writer(u'\n')
        if post.meta('keywords'):
            __M_writer(u'        <meta name="keywords" content="')
            __M_writer(filters.html_escape(unicode(post.meta('keywords'))))
            __M_writer(u'">\n')
        __M_writer(u'    <meta name="author" content="')
        __M_writer(unicode(post.author()))
        __M_writer(u'">\n    ')
        __M_writer(unicode(helper.open_graph_metadata(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.twitter_card_information(post)))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.meta_translations(post)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 7, "129": 8, "130": 8, "131": 9, "132": 10, "133": 10, "134": 10, "135": 12, "136": 12, "137": 12, "138": 13, "139": 13, "140": 14, "141": 14, "142": 15, "143": 15, "149": 143, "23": 2, "26": 3, "29": 4, "35": 0, "53": 2, "54": 3, "55": 4, "56": 5, "61": 16, "66": 39, "72": 18, "86": 18, "87": 20, "88": 20, "89": 23, "90": 23, "91": 23, "92": 23, "93": 24, "94": 24, "95": 25, "96": 25, "97": 27, "98": 27, "99": 30, "100": 30, "101": 32, "102": 32, "103": 33, "104": 34, "105": 34, "106": 34, "107": 36, "108": 36, "109": 36, "110": 38, "111": 38, "117": 7}, "uri": "post.tmpl", "filename": "themes/zen/templates/post.tmpl"}
__M_END_METADATA
"""
