# Using Puppet, install puppet-lint.

#package { 'puppet-lint':
#    ensure   => '2.5.0',
#    name     => 'puppet-lint',
#    provider => 'gem',
#    source   => 'http://rubygems.org',
#}

package { 'flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3',,
}
