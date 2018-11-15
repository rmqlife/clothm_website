# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522989287.627755
_enable_loop = True
_template_filename = u'themes/zen/templates/index.tmpl'
_template_uri = u'index.tmpl'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace(u'arusahni', context._clean_inheritance_tokens(), templateuri=u'arusahni_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, u'arusahni')] = ns

    ns = runtime.TemplateNamespace(u'helper', context._clean_inheritance_tokens(), templateuri=u'index_helper.tmpl', callables=None,  calling_uri=_template_uri)
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
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
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
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')
        for post in posts:
            __M_writer(u'        <div class="post">\n            <h1 class="title"><a href="')
            __M_writer(unicode(post.permalink()))
            __M_writer(u'">')
            __M_writer(unicode(post.title()))
            __M_writer(u'</a></h1>\n            <div class="meta">\n                <div class="authordate">\n                    <time class="timeago" datetime="')
            __M_writer(unicode(post.date.isoformat()))
            __M_writer(u'">')
            __M_writer(unicode(post.formatted_date(date_format)))
            __M_writer(u'</time>\n                </div>\n                <div class="stats">\n')
            if not post.meta('nocomments'):
                __M_writer(u'                    ')
                __M_writer(unicode(comments.comment_link(post.permalink(), post.base_path)))
                __M_writer(u'\n')
            __M_writer(u'                </div>\n            ')
            __M_writer(unicode(arusahni.html_tags(post)))
            __M_writer(u'\n            </div>\n            <div class="body">\n')
            if index_teasers:
                __M_writer(u'                ')
                __M_writer(unicode(post.text(teaser_only=True)))
                __M_writer(u'\n')
            else:
                __M_writer(u'                ')
                __M_writer(unicode(post.text(teaser_only=False)))
                __M_writer(u'\n')
            __M_writer(u'            </div>\n        </div>\n')
        __M_writer(u'    ')
        __M_writer(unicode(helper.html_pager()))
        __M_writer(u'\n    ')
        __M_writer(unicode(comments.comment_link_script()))
        __M_writer(u'\n    ')
        __M_writer(unicode(helper.mathjax_script(posts)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "50": 2, "51": 3, "52": 4, "53": 5, "58": 34, "64": 7, "78": 7, "79": 8, "80": 9, "81": 10, "82": 10, "83": 10, "84": 10, "85": 13, "86": 13, "87": 13, "88": 13, "89": 16, "90": 17, "91": 17, "92": 17, "93": 19, "94": 20, "95": 20, "96": 23, "97": 24, "98": 24, "99": 24, "100": 25, "101": 26, "102": 26, "103": 26, "104": 28, "105": 31, "106": 31, "107": 31, "108": 32, "109": 32, "110": 33, "111": 33, "117": 111}, "uri": "index.tmpl", "filename": "themes/zen/templates/index.tmpl"}
__M_END_METADATA
"""
