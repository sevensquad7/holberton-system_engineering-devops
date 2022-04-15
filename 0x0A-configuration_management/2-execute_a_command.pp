# Execute a command
exec { 'KILLMENOW':
  command   => 'pkill -f killmenow',
  provider  => 'shell'
}
