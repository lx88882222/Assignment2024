add_rules("mode.debug", "mode.release")
add_requires("nlohmann_json", "cpr")

target("fetch_webpage")
    set_kind("binary")
    set_languages("c++17")
    add_files("src/*.cpp")
    add_packages("nlohmann_json", "cpr")
    set_rundir("$(projectdir)")
