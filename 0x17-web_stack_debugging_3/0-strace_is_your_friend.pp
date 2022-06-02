# Once you find the issue, fix it and then automate it using Puppet
# (instead of using Bash as you were previously doing).
exec { 'correct_error':
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => shell
}
