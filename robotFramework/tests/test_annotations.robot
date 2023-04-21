*** Settings ***
Documentation      Annotation tests
Library            testit_adapter_robotframework.TMSLibrary
Library            steps.py

*** Variables ***
${NUMBER}          1
${VALUE}           String01

*** Test Cases ***
Without annotation success
    Return True

Without annotation failed
    Return False

With external id annotation success
    [Tags]  testit.externalID:With_external_id_annotation_success
    Return True

With external id annotation failed
    [Tags]  testit.externalID:With_external_id_annotation_failed
    Return False

With display name annotation success
    [Tags]  testit.displayName:With_display_name_annotation_success_display_name
    Return True

With display name annotation failed
    [Tags]  testit.displayName:With_display_name_annotation_failed_display_name
    Return False

With title annotation success
    [Tags]  testit.title:With_title_annotation_success_title
    Return True

With title annotation failed
    [Tags]  testit.title:With_title_annotation_failed_title
    Return False

With description annotation success
    [Tags]  testit.description:With_description_annotation_success
    Return True

With description annotation failed
    [Tags]  testit.description:With_description_annotation_failed
    Return False

With labels annotation success
    [Tags]  testit.labels:${{['Label1', 'Label2']}}
    Return True

With labels annotation failed
    [Tags]  testit.labels:${{['Label1', 'Label2']}}
    Return False

With links annotation success
    [Tags]  testit.links:${{{"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}}}
    ...     testit.links:${{{"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}}}
    Return True

With links annotation failed
    [Tags]  testit.links:${{{"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}}}
    ...     testit.links:${{{"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}}}
    Return False

With workitemids annotation success
    [Tags]  testit.workitemsID:${{[123, '321']}}
    Return True

With workitemids annotation failed
    [Tags]  testit.workitemsID:${{[123, '321']}}
    Return False

With all annotations success
    [Tags]  testit.externalID:With_all_annotations_success
    ...     testit.displayName:With_all_annotations_success_display_name
    ...     testit.title:With_all_annotations_success_title
    ...     testit.description:With_all_annotations_success
    ...     testit.labels:${{['Label1', 'Label2']}}
    ...     testit.links:${{{"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}}}
    ...     testit.links:${{{"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}}}
    ...     testit.workitemsID:${{[123, '321']}}
    Return True

With all annotations failed
    [Tags]  testit.externalID:With_all_annotations_failed
    ...     testit.displayName:With_all_annotations_failed_display_name
    ...     testit.title:With_all_annotations_failed_title
    ...     testit.description:With_all_annotations_failed
    ...     testit.labels:${{['Label1', 'Label2']}}
    ...     testit.links:${{{"url":"https://test01.example","title":"Example01","description":"Example01_description","type":"Issue"}}}
    ...     testit.links:${{{"url":"https://test02.example","title":"Example02","description":"Example02_description","type":"Issue"}}}
    ...     testit.workitemsID:${{[123, '321']}}
    Return False

Parametrized test success
    [Tags]  testit.externalID:parametrized_test_${NUMBER}_${VALUE}_success
    ...     testit.displayName:parametrized_test_${NUMBER}_${VALUE}_success_display_name
    ...     testit.title:parametrized_test_${NUMBER}_${VALUE}_success_title
    ...     testit.description:parametrized_test_${NUMBER}_${VALUE}_success
    Get Parameters ${NUMBER} ${VALUE}
    Return True

Parametrized test failed
    [Tags]  testit.externalID:parametrized_test_${NUMBER}_${VALUE}_failed
    ...     testit.displayName:parametrized_test_${NUMBER}_${VALUE}_failed_display_name
    ...     testit.title:parametrized_test_${NUMBER}_${VALUE}_failed_title
    ...     testit.description:parametrized_test_${NUMBER}_${VALUE}_failed
    Get Parameters ${NUMBER} ${VALUE}
    Return False
