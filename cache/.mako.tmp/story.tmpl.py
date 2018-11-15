# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522989287.966418
_enable_loop = True
_template_filename = u'themes/zen/templates/story.tmpl'
_template_uri = u'story.tmpl'
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
    return runtime._inherit_from(context, u'post.tmpl', _template_uri)
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
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
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
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        arusahni = _mako_get_namespace(context, 'arusahni')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<article class="storypage" itemscope="itemscope" itemtype="http://schema.org/Article">\n    <header>\n        ')
        __M_writer(unicode(arusahni.html_title()))
        __M_writer(u'\n        ')
        __M_writer(unicode(arusahni.html_translations(post)))
        __M_writer(u'\n    </header>\n    <div itemprop="articleBody text">\n    ')
        __M_writer(unicode(post.text()))
        __M_writer(u'\n    </div>\n')
        if site_has_comments and enable_comments and not post.meta('nocomments'):
            __M_writer(u'        <section class="comments">\n        <h2>')
            __M_writer(unicode(messages("Comments")))
            __M_writer(u'</h2>\n        ')
            __M_writer(unicode(comments.comment_form(post.permalink(absolute=True), post.title(), post.base_path)))
            __M_writer(u'\n        </section>\n')
        __M_writer(u'</article>\n')
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
        if post.description():
            __M_writer(u'        <meta name="description" itemprop="description" content="')
            __M_writer(unicode(post.description()))
            __M_writer(u'">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"128": 13, "129": 14, "130": 14, "131": 15, "132": 15, "133": 16, "134": 17, "135": 17, "136": 17, "142": 136, "23": 2, "26": 3, "29": 4, "35": 0, "54": 2, "55": 3, "56": 4, "57": 5, "62": 19, "67": 37, "73": 21, "87": 21, "88": 24, "89": 24, "90": 25, "91": 25, "92": 28, "93": 28, "94": 30, "95": 31, "96": 32, "97": 32, "98": 33, "99": 33, "100": 36, "106": 7, "117": 7, "118": 8, "119": 8, "120": 9, "121": 10, "122": 10, "123": 10, "124": 12, "125": 12, "126": 12, "127": 13}, "uri": "story.tmpl", "filename": "themes/zen/templates/story.tmpl"}
__M_END_METADATA
"""
