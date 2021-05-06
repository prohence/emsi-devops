# Puppet manifest file to install nginx
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file { '/var/www/html/404.html':
  content => 'Ceci n\'est pas une page',
}

file_line { 'Add redirection, 301':
  path   => '/etc/nginx/sites-available/default',
  ensure => 'present',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me http://github.com/prohence permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
