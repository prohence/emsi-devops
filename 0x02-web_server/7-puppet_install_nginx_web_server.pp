# Puppet manifest file to install nginx

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'Add redirection, 301':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'listen [::]:80 default_server;',
  line   => 'rewrite ^/redirect_me http://github.com/prohence permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
