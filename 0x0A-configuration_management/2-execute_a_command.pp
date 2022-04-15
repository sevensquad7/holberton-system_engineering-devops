# Execute a command
exec { 'KILLMENOW':
  command  => 'pkill -f killmenow',
  path     => '/usr/bin/pkill'
}
