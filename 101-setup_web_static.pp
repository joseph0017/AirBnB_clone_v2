# Puppet script that sets up your web servers for the deployment of web_static

# Nginx configuration => /etc/nginx/sites-available/default
$nginx_configuration = "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        #The header
        add_header X-Served-By $HOSTNAME;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
	
	error_page 404 /page_not_found.html;
        location /404 {
                root /var/www/html;
		internal;
        }
}"

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

file { '/data':
  ensure  => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "dummy alx content"
}

exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_configuration
} 

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "well hello there!"
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
