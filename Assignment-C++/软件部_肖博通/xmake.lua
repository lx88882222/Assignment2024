add_requires("rapidjson", "cpr")

target("cpphomework")
    set_kind("binary")
    set_languages("c++17")
    add_files("src/*.cpp")
    add_packages("rapidjson", "cpr")
    set_rundir("$(projectdir)")