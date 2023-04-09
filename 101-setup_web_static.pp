# Puppet script that sets up your web servers for the deployment of web_static

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
} 

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "well hello there!"
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
