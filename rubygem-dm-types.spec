#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-dm-types
Version  : 1.2.2
Release  : 3
URL      : https://rubygems.org/downloads/dm-types-1.2.2.gem
Source0  : https://rubygems.org/downloads/dm-types-1.2.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-addressable
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-dm-core
BuildRequires : rubygem-dm-migrations
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support

%description
= dm-types
DataMapper plugin providing many extra types for use in data models.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n dm-types-1.2.2
gem spec %{SOURCE0} -l --ruby > rubygem-dm-types.gemspec

%build
gem build rubygem-dm-types.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
dm-types-1.2.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/dm-types-1.2.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/README.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/dm-types.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/api_key.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/bcrypt_hash.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/comma_separated_list.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/csv.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/enum.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/epoch_time.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/file_path.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/flag.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/ip_address.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/json.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/paranoid/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/paranoid_boolean.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/paranoid_datetime.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/regexp.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/slug.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/support/dirty_minder.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/support/flags.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/uri.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/uuid.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/lib/dm-types/yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/api_user.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/article.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/bookmark.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/invention.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/network_node.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/person.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/software_package.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/ticket.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/fixtures/tshirt.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/api_key_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/bcrypt_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/comma_separated_list_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/dirty_minder_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/enum_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/epoch_time_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/file_path_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/flag_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/ip_address_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/json_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/slug_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/uri_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/uuid_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/integration/yaml_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/rcov.opts
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/shared/flags_shared_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/shared/identity_function_group.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/spec.opts
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/bcrypt_hash_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/csv_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/enum_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/epoch_time_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/file_path_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/flag_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/ip_address_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/json_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/paranoid_boolean_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/paranoid_datetime_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/regexp_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/uri_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/uuid_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/spec/unit/yaml_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/tasks/spec.rake
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/tasks/yard.rake
/usr/lib64/ruby/gems/2.3.0/gems/dm-types-1.2.2/tasks/yardstick.rake
/usr/lib64/ruby/gems/2.3.0/specifications/dm-types-1.2.2.gemspec
