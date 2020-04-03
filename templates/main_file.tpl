Name:           patterns-zigzag
Version:        0
Release:        0
Summary:        Patterns for Zigzag Linux
License:        GPL-3.0
Group:          Metapackages
Url:            https://github.com/zigzag/zigzag-patterns
BuildRequires:  patterns-rpm-macros

%description
This package is used to build all patterns of Zigzag Linux

$pattern_sections

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns
for i in zigzag-{$all_patterns}; do
    echo "This file marks the pattern $$i to be installed." \
    >"%{buildroot}%{_docdir}/patterns/$$i.txt"
done

%changelog
