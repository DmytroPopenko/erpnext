import frappe

def get_context(context):
    # Отримати всі опубліковані блог-пости
    blog_posts = frappe.get_all('Blog Post', 
        filters={'published': 1}, 
        fields=['title', 'route', 'published_on', 'blog_intro', 'meta_image'],
        order_by="published_on desc"
    )
    
    # Додати блог-пости в контекст для рендерингу в шаблоні
    context.blog_posts = blog_posts

    # Ви також можете додати інші контексти, наприклад, мета-заголовки чи додаткову інформацію
    context.title = "News and Blog Posts"
