#include "mangle.h"
int fd_create_webview(const char *title, int wd, int hg, const char *url)
{
    webview::webview w(true, nullptr);
    w.set_title(title);
    w.set_size(wd, hg, WEBVIEW_HINT_NONE);

    w.navigate(url);
    w.run();
    return 0;
}