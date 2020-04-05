################################################################################

%package $pattern_name
%pattern_basetechnologies
Summary:        $pattern_summary
Group:          Metapackages
Provides:       pattern() = zigzag-$pattern_name
Provides:       pattern-icon() = pattern-basis
Provides:       pattern-order() = 1100
Provides:       pattern-visible()
$extra_meta

$required_packages

%description $pattern_name
$pattern_description

%files $pattern_name
%dir %{_docdir}/patterns
%{_docdir}/patterns/zigzag-$pattern_name.txt

