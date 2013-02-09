wxMarkdown
==========

Views a markdown file as html. The executable is called ```wxmdv.py```.

wxMarkdown uses webkit for displaying the html content. So all the
nifty stuff, which webkit can do, wxMarkdown can do also. Such like video playback, 
displaying images, etc.
But wxMarkdown does not follow links, yet.

Javascript is disabled by default for security reasons. And yet you can't enable it,
unless you change the code.

Requirements
------------

As long as wxMarkdown uses gtk-webkit, the GTK port of wxwidgets is inevitable.
Thus means wxMarkdown will only run on platforms where wxGTK is available and installed.
This will change with the upcoming major version of wxwidgets, where a platform independent
modern html component is available. But until then, there's no other way. And
*wxHtmlWindow* is no alternative, seriously!

 * wxpython 2.8.*
 * markdown2 or markdown
 * chardet
