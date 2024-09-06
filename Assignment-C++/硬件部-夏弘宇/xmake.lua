add_rules("mode.debug", "mode.release")
add_requires("nlohmann_json")  
add_requires("libcurl")

target("HttpReader")
    set_kind("binary")
    add_files("src/*.cpp")
    add_packages("nlohmann_json", "libcurl")  -- 使用 xmake 管理库