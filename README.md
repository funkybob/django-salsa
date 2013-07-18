django-salsa
============

An attempt at a fresh, new CMS for Django

The Plan
========

A web site is a collection of Pages in an hierarchy.

Each page typically renders a Template, into which it will place Fragments of content.

Some Fragments will interact with requests.

Constraints & Assumptions
~~~~~~~~~~~~~~~~~~~~~~~~~

+ Postgres

    Beyond the interminable arguments, it provides us with Common Table Expressions [used for efficient Trees], and hstore [used for Attributes]

+ No django.contrib.admin

    Django's Admin, in being so powerful, is a common trap for developers.  Whilst it gives you a short-cut to a "good enough" management console, it also subtly influences your thinking, especially when it comes to schema design.

Design Objects
==============

Pages
~~~~~

Each Page is positioned in an ordered Tree structure.  Combining its ``url step`` with that of its parents, down to the root, forms its URI.

A Page is assigned a Template by the Editor.

Additionally, a Page may have any number of Fragments bound to it by user-defined names.  These Fragments are then available in the template, accessible by name.

Templates
~~~~~~~~~

These are simply Django templates.  Templates may also have {% fragment %} tags which indicate where in them a given named fragment will be rendered.

Fragments
~~~~~~~~~

A Fragment is a piece of content which may be bound to one or many Pages.  It may have a different name on each page it is bound to.

[[ Common fragments?  Default fragments?  Page Fragment templates? ]]

Fragments may also hook into the request handling process, allowing, for instance, form processing, list filtering, or any other actions.  Because the order in which these actions are performed is important, Fragments are bound to a page in an ordered fashion.

Various Fragment types may be installed beyond the basics provided with the base install.  It is Framgnet types, not Page types, which provide the pluggable functionality of the system.


Console
=======

The whole site content is managed through the Console.

This will be a modern, JavaScript driven UI custom tailored to the needs of the system.

When editing a Page, a list of Templates available will be provided.  When selected, the Template is scanned for {% fragment %} tags, allowing the Console to show a list of fragment names used in the chosen template.  The user is not required to fill all fragment names, nor to provide only fragments of those names.

Template editing will be provided, using a smart, syntax hilighting editor [[ CodeMirror ]]

File Management
~~~~~~~~~~~~~~~

Ideally, a system of equivalent functionality to elFinder will be provided for managing static/media files, as well as editing Templates.

This provides a familiar, drag-n-drop, multi-pane approach to file management, as well as bulk up-/down-loading.

