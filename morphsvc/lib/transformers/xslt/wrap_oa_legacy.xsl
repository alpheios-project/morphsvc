<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:oac="http://www.openannotation.org/ns/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:cnt="http://www.w3.org/2008/content#"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    version="1.0">

    <!-- this template wraps a treebank annotation in an OA container.

         parameters
            e_datetime - the datetime of the serialization
            e_collection - the urn of the CITE collection which the annotation is/will be a member of
            e_docuri - target of the annotation, if supplied will override anything in the template
    -->

    <xsl:param name="e_datetime"/>
    <xsl:param name="e_annotationuri"/>
    <xsl:param name="e_worduri"/>
    <xsl:param name="e_agenturi"/>
    <xsl:param name="e_agentrights"/>

    <xsl:output indent="yes" encoding="UTF-8"></xsl:output>
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">

        <xsl:element name="rdf:RDF">
            <xsl:element name="oac:Annotation">
                <xsl:attribute name="rdf:about"><xsl:value-of select="$e_annotationuri"/></xsl:attribute>
                <xsl:element name="dcterms:creator">
                    <xsl:element name="foaf:Agent">
                        <xsl:attribute name="rdf:about"><xsl:value-of select="$e_agenturi"/></xsl:attribute>
                    </xsl:element>
                </xsl:element>
                <xsl:element name="dcterms:created">
                    <xsl:value-of select="$e_datetime"/>
                </xsl:element>
                <xsl:element name="dc:rights">
                    <xsl:value-of select="$e_agentrights"/>
                </xsl:element>
                <xsl:element name="oac:hasTarget">
                    <xsl:element name="rdf:Description">
                        <xsl:attribute name="rdf:about"><xsl:value-of select="$e_worduri"/></xsl:attribute>
                    </xsl:element>
                </xsl:element>
                <xsl:element name="dc:title"/>
                <xsl:apply-templates select="//entry"></xsl:apply-templates>
            </xsl:element>
        </xsl:element>
    </xsl:template>

    <xsl:template match="entry">
        <xsl:variable name="bodyid" select="concat('urn:uuid:',generate-id(.))"/>
        <xsl:element name="oac:hasBody">
            <xsl:attribute name="rdf:resource"><xsl:value-of select="$bodyid"/></xsl:attribute>
        </xsl:element>
        <xsl:element name="oac:Body">
            <xsl:attribute name="rdf:about"><xsl:value-of select="$bodyid"/></xsl:attribute>
            <xsl:element name="rdf:type">
                <xsl:attribute name="rdf:resource">cnt:ContentAsXML</xsl:attribute>
            </xsl:element>
            <xsl:element name="cnt:rest">
                <xsl:copy-of select="."/>
            </xsl:element>
        </xsl:element>
    </xsl:template>
</xsl:stylesheet>
