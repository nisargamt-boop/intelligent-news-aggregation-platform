# Deployment Checklist

## 1. Server Setup
- [ ] Install Python 3.x
- [ ] Install Redis
- [ ] Install Nginx
- [ ] Create a virtual environment
- [ ] Install required packages: `pip install -r requirements.txt`
- [ ] Install gunicorn: `pip install gunicorn`

## 2. Django Configuration
- [ ] Update ALLOWED_HOSTS in settings_prod.py with your domain
- [ ] Generate new SECRET_KEY and update in settings_prod.py
- [ ] Set DEBUG = False in settings_prod.py
- [ ] Configure database settings for production
- [ ] Run migrations: `python manage.py migrate`
- [ ] Collect static files: `python manage.py collectstatic`
- [ ] Create superuser: `python manage.py createsuperuser`

## 3. SSL/TLS Setup
- [ ] Obtain SSL certificate (Let's Encrypt recommended)
- [ ] Update Nginx configuration with SSL certificate paths
- [ ] Configure SSL settings in Django

## 4. Service Setup
- [ ] Copy news-aggregator.service to /etc/systemd/system/
- [ ] Update paths in news-aggregator.service
- [ ] Enable and start the service:
  ```bash
  sudo systemctl enable news-aggregator
  sudo systemctl start news-aggregator
  ```

## 5. Nginx Setup
- [ ] Install Nginx
- [ ] Copy nginx.conf to /etc/nginx/sites-available/
- [ ] Create symbolic link to sites-enabled
- [ ] Test and reload Nginx configuration:
  ```bash
  sudo nginx -t
  sudo systemctl reload nginx
  ```

## 6. Redis & Celery Setup
- [ ] Install Redis
- [ ] Configure Redis password
- [ ] Update Celery settings with Redis password
- [ ] Set up Celery service
- [ ] Set up Celery Beat service

## 7. Monitoring Setup
- [ ] Set up logging
- [ ] Configure backup system
- [ ] Set up monitoring (e.g., Prometheus/Grafana)
- [ ] Configure error reporting (e.g., Sentry)

## 8. Security Checklist
- [ ] Configure firewall (UFW)
- [ ] Set up fail2ban
- [ ] Configure automatic security updates
- [ ] Set up regular backup system
- [ ] Review Django security checklist
- [ ] Configure rate limiting

## 9. Performance Optimization
- [ ] Configure caching
- [ ] Enable Gzip compression
- [ ] Set up CDN (if needed)
- [ ] Configure static file serving
- [ ] Optimize database queries

## 10. Testing
- [ ] Test all functionality
- [ ] Load test the application
- [ ] Test backup and restore procedures
- [ ] Test SSL configuration
- [ ] Verify logging
- [ ] Check error handling