# Puppet script that sets up your web servers for the deployment of web_static

$directories = ['/data/','/data/web_static','/data/web_static/shared','/data/web_static/releases','/data/web_static/releases/test']

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

file {$directories:
  ensure  => 'directory',
  recurse => 'remote',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0777'
}

file {'/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test'
}

file {'/data/web_static/releases/test/index.html':
  ensure  => 'present'
  content => 'dummy alx content'
}

exec {'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

file_line {'deploy':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _',
}

service {'nginx':
  ensure => 'running'
}

exec { 'nginx restart':
  path => '/etc/init.d/'
}
