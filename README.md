# dashing-widgets
Django dashing custom widgets for AdNabu

depends on [django-dashing](https://github.com/talpor/django-dashing)

# add dashing widgets to urls.py
```python
urlpatterns = patterns('',
    # Examples:
    url(r'^blog/', include('blog.urls')),
    url(r'^dashing/widgets/', include('dashing_widgets.urls', namespace='dashing_widgets')),
)
```

# changes to dashing-config.js
```javascript
dashboard.addWidget('new_users_widget', 'Number', {
    getData: function () {
        var self = this;
        $.get('/dashing/widgets/users', function(data) {
            $.extend(self.data, data);
        });
    },
    interval: 30000
});
```

# add dashing widgets to settings.py
```python
INSTALLED_APPS = (
    '....',
    'dashing_widgets',
)
```
