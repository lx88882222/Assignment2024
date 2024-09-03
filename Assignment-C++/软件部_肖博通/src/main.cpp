#include <iostream>
#include <fstream>
#include <rapidjson/document.h>
#include <rapidjson/istreamwrapper.h>
#include <cpr/cpr.h>

int main() {
    // 读取 config.json 文件
    std::ifstream config_file("config.json");
    if (!config_file.is_open()) {
        std::cerr << "Cannot open config.json " << std::endl;
        return 1;
    }

    rapidjson::IStreamWrapper isw(config_file);
    rapidjson::Document config;
    config.ParseStream(isw);
    if (config.HasParseError()) {
        std::cerr << "fail to process config.json " << std::endl;
        return 1;
    }

    std::string url = config["url"].GetString();

    // 使用 cpr 访问网址
    cpr::Response r = cpr::Get(cpr::Url{url});
    if (r.error) {
        std::cerr << "https request fail " << r.error.message << std::endl;
        return 1;
    }

    // 将网页内容保存到文件
    std::ofstream output_file("output.html");
    if (!output_file.is_open()) {
        std::cerr << "cannot build output.html 文件" << std::endl;
        return 1;
    }
    output_file << r.text;

    std::cout << "website has been saved to output.html" << std::endl;
    return 0;
}