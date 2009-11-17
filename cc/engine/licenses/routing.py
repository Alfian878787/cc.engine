from routes.route import Route

licenses_routes = [
    Route("licenses_index", "/licenses/",
          controller="cc.engine.licenses.views:licenses_view"),
    Route("license_deed",
          "/licenses/{code}/{version}/",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_deed_lang",
          "/licenses/{code}/{version}/deed.{target_lang}",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_rdf",
          "/licenses/{code}/{version}/rdf",
          controller="cc.engine.licenses.views:license_rdf_view"),
    Route("license_legalcode",
          "/licenses/{code}/{version}/legalcode",
          controller="cc.engine.licenses.views:license_legalcode_view"),
    Route("license_legalcode_plain",
          "/licenses/{code}/{version}/legalcode-plain",
          controller="cc.engine.licenses.views:license_legalcode_plain_view"),
    Route("license_deed_jurisdiction",
          "/licenses/{code}/{version}/{jurisdiction}/",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_deed_lang_jurisdiction",
          "/licenses/{code}/{version}/{jurisdiction}/deed.{target_lang}",
          controller="cc.engine.licenses.views:license_deed_view"),
    Route("license_rdf_jurisdiction",
          "/licenses/{code}/{version}/{jurisdiction}/rdf",
          controller="cc.engine.licenses.views:license_rdf_view"),
    Route("license_legalcode_jurisdiction",
          "/licenses/{code}/{version}/jurisdiction}/legalcode",
          controller="cc.engine.licenses.views:license_legalcode_view"),
    Route("license_legalcode_plain_jurisdiction",
          "/licenses/{code}/{version}/jurisdiction}/legalcode-plain",
          controller="cc.engine.licenses.views:license_legalcode_plain_view")]
