# Copyright 2019 Nokia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Name:       ansible-role-ntp
Version:    0.4.0.2.g4fc673c
Release:    1%{?dist}
Summary:    This role enables users to install and configure ntp on their hosts.

Vendor:     %{_platform_vendor} and Benno Joy, René Moser modified
License:    %{_platform_licence} and BSD
URL:        https://github.com/resmo/ansible-role-ntp
Source0:    https://github.com/resmo/%{name}/archive/%{sha}.zip
Patch0:     0001-initial.patch

BuildArch:      noarch
BuildRequires:  python python-setuptools
Requires:   ansible => 1.4

%global sha 4fc673cfdf6cb3704a8be10cd10728a21be8f1bb

%description

%prep
%autosetup -n %{name}-%{sha} -p 1

%install
mkdir -p %{buildroot}/etc/ansible/roles/ntp

rsync -av --exclude ansible-role-ntp.spec \
          --exclude .travis.yml \
          --exclude .gitignore \
          --exclude README.md \
          --exclude *tests* \
          --exclude .git \
          --exclude .gitreview \
          . %{buildroot}/etc/ansible/roles/ntp/
%files
%defattr(0755,root,root)
/etc/ansible/roles/ntp/
